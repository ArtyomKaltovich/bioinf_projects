- install QIIME 2


    $ wget https://data.qiime2.org/distro/core/qiime2-2020.2-py36-linux-conda.yml
    $ conda env create -n qiime2-2020.2 --file qiime2-2020.2-py36-linux-conda.yml
    $ rm qiime2-2020.2-py36-linux-conda.yml
    $ source activate qiime2-2020.2
    
- qiimeing


    $ qiime tools import   --type 'SampleData[SequencesWithQuality]'   --input-path manifest.tsv   --output-path sequences.qza   --input-format SingleEndFastqManifestPhred33V2
    Imported manifest.tsv as SingleEndFastqManifestPhred33V2 to sequences.qza
    $ qiime tools validate sequences.qza 
    Result sequences.qza appears to be valid at level=max.
    $ qiime demux summarize   --i-data sequences.qza   --o-visualization sequences.qzv


- Demultiplexing and QC


    $ qiime demux summarize --i-data sequences.qza --o-visualization sequences.qzv
    Saved Visualization to: sequences.qzv


- fastqc


    $ fastqc SRX351237_calculus_sra_data.fastq -t 4 -o ../fastqc/
    $ fastqc SRX351242_bone_sra_data.fastq -t 4 -o ../fastqc/
    
- Feature table construction (and more QC)

    $ qiime dada2 denoise-single --i-demultiplexed-seqs sequences.qza --p-trim-left 10 --p-trunc-len 169 --o-representative-sequences rep-seqs.qza --o-table table.qza --o-denoising-stats stats.qza
    Saved FeatureTable[Frequency] to: table.qza
    Saved FeatureData[Sequence] to: rep-seqs.qza
    Saved SampleData[DADA2Stats] to: stats.qza
    
    $ qiime metadata tabulate   --m-input-file stats.qza   --o-visualization stats.qzv

Result of filter:

| sample-id #q2:types | input numeric | filtered numeric | percentage of input passed filter numeric | denoised numeric | non-chimeric numeric | percentage of input non-chimeric numeric |
|---------------------|---------------|------------------|-------------------------------------------|------------------|----------------------|------------------------------------------|
| bone                | 5788          | 5544             | 95.78                                     | 5367             | 5367                 | 92.73                                    |
| calculus            | 5362          | 5158             | 96.2                                      | 5024             | 4715                 | 87.93                                    |

- FeatureTable and FeatureData summaries


    $ qiime feature-table summarize   --i-table table.qza   --o-visualization table.qzv   --m-sample-metadata-file sample-metadata.tsv
    Saved Visualization to: table.qzv

    $ qiime feature-table tabulate-seqs  --i-data rep-seqs.qza   --o-visualization rep-seqs.qzv
    qiime feature-table tabulate-seqs  --i-data rep-seqs.qza   --o-visualization rep-seqs.qzv

- https://docs.qiime2.org/2020.2/data-resources/ install classifier


    $ conda install --override-channels -c defaults scikit-learn=0.22.1

- download https://data.qiime2.org/2020.2/common/gg-13-8-99-nb-classifier.qza

- classification


    $ qiime feature-classifier classify-sklearn   --i-classifier gg-13-8-99-nb-classifier.qza   --i-reads rep-seqs.qza   --o-classification taxonomy.qza
    $ qiime metadata tabulate --m-input-file taxonomy.qza --o-visualization taxonomy.qzv
    $ qiime taxa barplot --i-table table.qza --i-taxonomy taxonomy.qza --m-metadata-file sample-metadata.tsv --o-visualization taxa-bar-plots.qzv

- download metagenome
- install


    $ conda install metaphlan2=2.7.8
    Specifications:

    - metaphlan2=2.7.8 -> python[version='>=2.7,<2.8.0a0']

    Your python: python=3.6.7

    $ conda install metaphlan

- run


    $ metaphlan G12_assembly.fna.gz --input_type fasta --nproc 4 > output.txt
    Downloading https://www.dropbox.com/sh/7qze7m7g9fe2xjg/AAA4XDP85WHon_eHvztxkamTa/file_list.txt?dl=1
    Downloading file of size: 0.00 MB
    0.01 MB 232.33 %   4.22 MB/sec  0 min -0 sec         
    Downloading https://www.dropbox.com/sh/7qze7m7g9fe2xjg/AAAyoJpOgcjop41VIHAGWIVLa/mpa_latest?dl=1
    Downloading file of size: 0.00 MB
    0.01 MB 31507.69 %   1.76 MB/sec  0 min -0 sec         
    Downloading MetaPhlAn database
    Please note due to the size this might take a few minutes
    
    File /home/my/miniconda3/envs/qiime2-2020.2/lib/python3.6/site-packages/metaphlan/metaphlan_databases/file_list.txt already present!
    Traceback (most recent call last):
      File "/home/my/miniconda3/envs/qiime2-2020.2/bin/metaphlan", line 10, in <module>
        sys.exit(main())
      File "/home/my/miniconda3/envs/qiime2-2020.2/lib/python3.6/site-packages/metaphlan/metaphlan.py", line 1187, in main
        pars['index'] = check_and_install_database(pars['index'], pars['bowtie2db'], pars['bowtie2_build'], pars['nproc'], pars['force_download'])
      File "/home/my/miniconda3/envs/qiime2-2020.2/lib/python3.6/site-packages/metaphlan/metaphlan.py", line 610, in check_and_install_database
        download_unpack_tar(FILE_LIST, index, bowtie2_db, bowtie2_build, nproc)
      File "/home/my/miniconda3/envs/qiime2-2020.2/lib/python3.6/site-packages/metaphlan/metaphlan.py", line 463, in download_unpack_tar
        url_tar_file = ls_f["mpa_" + download_file_name + ".tar"]
    KeyError: 'mpa_mpa_v30_CHOCOPhlAn_201901.tar'

- cloning grom git 


    $ git clone https://github.com/biobakery/MetaPhlAn.git

- run


    $ ~/bin/MetaPhlAn/metaphlan2.py G12_assembly.fna.gz --input_type fasta --nproc 4 > output.txt

- Comparison with samples from HMP


    $  for f in *.fasta; do ~/bin/MetaPhlAn/metaphlan2.py $f --input_type fasta --nproc 4 > ${f%}_profile.txt; done

- merging


    $ ~/bin/MetaPhlAn/utils/merge_metaphlan_tables.py *.fasta_profile.txt *.fasta_profile.txt > merge_output.txt

- heatmap


    ~/bin/MetaPhlAn/utils/metaphlan_hclust_heatmap.py  --in merge_output.txt --out heatmap.png -s log --top 50
    error occures, have to fix code - after it heatmap was created
