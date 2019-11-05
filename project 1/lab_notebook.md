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
  trimmomatic PE -phred33 amp_res_1.fastq amp_res_2.fastq output_paired_1.fasta output_unpaired_1.fasta output_paired_2.fasta output_unpaired_2.fasta LEADING:20 TRAILING:20 SLIDINGWINDOW:10:20 MINLEN:20
TrimmomaticPE: Started with arguments:
 -phred33 amp_res_1.fastq amp_res_2.fastq output_paired_1.fasta output_unpaired_1.fasta output_paired_2.fasta output_unpaired_2.fasta LEADING:20 TRAILING:20 SLIDINGWINDOW:10:20 MINLEN:20
Multiple cores found: Using 4 threads
Input Read Pairs: 455876 Both Surviving: 446259 (97.89%) Forward Only Surviving: 9216 (2.02%) Reverse Only Surviving: 273 (0.06%) Dropped: 128 (0.03%)
TrimmomaticPE: Completed successfully
  ```

  Zipping trimmonatic output files.

