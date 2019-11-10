05.11.2019 - creating git repo, downloading e.coli genome.

There is 1823504 lines in raw reads (wc -l commands),
which gives us 455876 reads in both files.

FastQC both files, there are several red labels:

  * [FAIL] Per base sequence quality:
    The doc says:
    >This module will raise a failure if the lower
    >quartile for any base is less than 5 or if the median for 
    >any base is less than 20.
    
    Actually it is not represented by the charts. (?!)

  * [FAIL] Per tile sequence quality
    > This module will issue a warning if any tile shows a mean Phred
    > score more than 5 less than the mean for that base across all tiles.

  Trimmonatic PE:

  ```
  $ trimmomatic PE -phred33 amp_res_1.fastq amp_res_2.fastq output_paired_1.fasta output_unpaired_1.fasta output_paired_2.fasta output_unpaired_2.fasta LEADING:20 TRAILING:20 SLIDINGWINDOW:10:20 MINLEN:20

TrimmomaticPE: Started with arguments:
 -phred33 amp_res_1.fastq amp_res_2.fastq output_paired_1.fasta output_unpaired_1.fasta output_paired_2.fasta output_unpaired_2.fasta LEADING:20 TRAILING:20 SLIDINGWINDOW:10:20 MINLEN:20
Multiple cores found: Using 4 threads
Input Read Pairs: 455876 Both Surviving: 446259 (97.89%) Forward Only Surviving: 9216 (2.02%) Reverse Only Surviving: 273 (0.06%) Dropped: 128 (0.03%)
TrimmomaticPE: Completed successfully
  ```

  Zipping trimmonatic output files.
  
11.11.2019 - alignment

BWA indexing:

    $ bwa index ecoli.fna 

BWA alignment:

    $ bwa mem ecoli.fna output_paired_1.fasta output_paired_2.fasta > alignment.sam

samtoolsing:

    $ samtools view -S -b alignment.sam > alignment.bam
    $ samtools flagstat alignment.bam
    
    892776 + 0 in total (QC-passed reads + QC-failed reads)
    0 + 0 secondary
    258 + 0 supplementary
    0 + 0 duplicates
    891649 + 0 mapped (99.87% : N/A) <- mapped percent
    892518 + 0 paired in sequencing
    446259 + 0 read1
    446259 + 0 read2
    888554 + 0 properly paired (99.56% : N/A)
    890412 + 0 with itself and mate mapped
    979 + 0 singletons (0.11% : N/A)
    0 + 0 with mate mapped to a different chr
    0 + 0 with mate mapped to a different chr (mapQ>=5)

Sort and index BAM file

    $ samtools sort alignment.bam -o alignment_sorted.bam
    $ samtools index alignment_sorted.bam

Variant calling    

    $ samtools mpileup -f ecoli.fna alignment_sorted.bam >  my.mpileup
    $ java -jar ../VarScan.v2.4.4.jar  mpileup2snp my.mpileup --min-var-freq 0.01 --variants --output-vcf 1 > VarScan_results_0.01.vcf
    $ java -jar ../VarScan.v2.4.4.jar  mpileup2snp my.mpileup --min-var-freq 0.05 --variants --output-vcf 1 > VarScan_results_0.05.vcf
    $ java -jar ../VarScan.v2.4.4.jar  mpileup2snp my.mpileup --min-var-freq 0.10 --variants --output-vcf 1 > VarScan_results_0.10.vcf
