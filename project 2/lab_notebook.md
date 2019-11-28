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

    $ samtools mpileup -d 100000 -f reference.fasta roommate_indexed.bam -o roommate.mpileup
    $ java -jar ../../VarScan.v2.4.4.jar mpileup2snp roommate.mpileup --min-var-freq 0.95 --variants --output-vcf 1 > roommate.vcf
    $ cat roommate.vcf | awk 'FNR==1{print "position,base,alt_base,frequency";next} NR>24 {split($10,a,":"); print $2, $4, $5, a[7]}' OFS=, > roommate.csv
    $ java -jar ../../VarScan.v2.4.4.jar mpileup2snp roommate.mpileup --min-var-freq 0.001 --variants --output-vcf 1 > roommate_0.001.vcf
    $ cat roommate_0.001.vcf | awk 'FNR==1{print "position,base,alt_base,frequency";next} NR>24 {split($10,a,":"); print $2, $4, $5, a[7]}' OFS=, > roommate_0.001.csv
    
#28.11.2019 - sequencing error

Creating sh script for alignning `data/align.sh`

Creating python script for rare SNP filtering `data/mead_and_std.py`.
id - is index pos is in `roommate_0.001.csv`.

    id   position base alt_base  frequency
    0         72    A        G      99.96%
    1        117    C        T      99.82%  - Epitope D
    4        307    C        T       0.94%  - Epitope C
    10       774    T        C      99.96%
    14       999    C        T      99.86%
    18      1260    A        C      99.94%
    20      1458    T        C       0.84%
    
Creating python script for finding PCR errors `data/pcr_errors.py`
(just find position all 3 files have SNP)

    position base alt_base  frequency
      165    T        C       0.24%
      183    A        G       0.30%
      216    A        G       0.22%
      218    A        G       0.28%
      222    T        C       0.26%
      254    A        G       0.25%
      276    A        G       0.22%
      340    T        C       0.23%
      356    A        G       0.22%
      370    A        G       0.21%
      409    T        C       0.22%
      414    T        C       0.28%
      421    A        G       0.18%
      463    A        G       0.19%
      660    A        G       0.20%
      670    A        G       0.29%
      691    A        G       0.23%
      722    A        G       0.23%
      744    A        G       0.21%
      859    A        G       0.27%
      915    T        C       0.26%
      987    A        G       0.22%
     1031    A        G       0.28%
     1056    T        C       0.20%
     1086    A        G       0.33%
     1213    A        G       0.24%
     1264    T        C       0.26%
     1280    T        C       0.25%
     1358    A        G       0.26%
     1398    T        C       0.20%
     1421    A        G       0.31%
     1460    A        G       0.34%
     1482    A        G       0.24%
