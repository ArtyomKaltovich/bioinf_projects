- install QIIME 2


    $ wget https://data.qiime2.org/distro/core/qiime2-2020.2-py36-linux-conda.yml
    $ conda env create -n qiime2-2020.2 --file qiime2-2020.2-py36-linux-conda.yml
    $ rm qiime2-2020.2-py36-linux-conda.yml
    $ source activate qiime2-2020.2
    
- qiimeing


    $ qiime tools import   --type 'SampleData[SequencesWithQuality]'   --input-path manifest.tsv   --output-path sequences.qza   --input-format SingleEndFastqManifestPhred33V2
    Imported manifest.tsv as SingleEndFastqManifestPhred33V2 to sequences.qza
