# 17.11.2019 - Get WHO info, download samples

Suggested for vaccination: http://www.euro.who.int/en/health-topics/communicable-diseases/influenza/publications/2017/recommended-composition-of-influenza-virus-vaccines-for-use-in-the-2017-2018-northern-hemisphere-influenza-season-2017

>It is recommended that trivalent vaccines for use in the 2017-2018 northern hemisphere influenza season contain the following:
>
>* an A/Michigan/45/2015 (H1N1)pdm09-like virus;
>* an A/Hong Kong/4801/2014 (H3N2)-like virus; and
>* a B/Brisbane/60/2008-like virus.
>
>It is recommended that quadrivalent vaccines containing two influenza B viruses contain the above three viruses and a B/Phuket/3073/2013-like virus.

Download reference genome and put it to data/reference.fasta

Download sequenced genome and put it to data/SRR1705851.fastq.gz

Unpucking it to data/roommate.fastq and 

Fastqcing:

    $ cd data
    $ fastqc SRR1705851.fastq

>Sequences flagged as poor quality	0

So no trimmonatic is needed.

The error raised traits:

* Duplicate Sequences
>This module will issue a error if non-unique sequences make up more than 50% of the total. 

* Per Base Sequence Content
> This module will fail if the difference between A and T, or G and C is greater than 20% in any position. 

This is ok for deep sequencing.

# 25.11.2019 - indexing and aligning

    $ bwa index reference.fasta
    $ bwa mem reference.fasta roommate.fastq | samtools view -S -b - | samtools sort -o roommate - 

Number of mapped reads:

    $ samtools view roommate.bam -c

361349 of 358265 were mapped.

    $ samtools flagstat roommate.bam   

    361349 + 0 in total (QC-passed reads + QC-failed reads)
    0 + 0 secondary
    3084 + 0 supplementary
    0 + 0 duplicates
    361116 + 0 mapped (99.94% : N/A)
    0 + 0 paired in sequencing
    0 + 0 read1
    0 + 0 read2
    0 + 0 properly paired (N/A : N/A)
    0 + 0 with itself and mate mapped
    0 + 0 singletons (N/A : N/A)
    0 + 0 with mate mapped to a different chr
    0 + 0 with mate mapped to a different chr (mapQ>=5)
    
list of non unique read was constacted and saved to data\non_unique_reads.txt

    $ samtools view roommate.bam | awk '{print $1}' | sort | uniq -d > non_unique_reads.txt
    
Sort and index BAM file

    $ samtools sort roommate.bam -o roommate_indexed.bam 
    $ samtools index roommate_indexed.bam 

Variant calling    

    $ samtools mpileup -f reference.fasta roommate_indexed.bam -o roommate.mpileup 
