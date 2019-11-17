17.11.2019 - Get WHO info, download samples

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

Unpucking it to data/SRR1705851.fastq and 

Fastqcing:

    cd data
    fastqc SRR1705851.fastq

>Sequences flagged as poor quality	0

So no trimmonatic is needed.

The error raised traits:

* Duplicate Sequences
>This module will issue a error if non-unique sequences make up more than 50% of the total. 

We guess this is ok for deep sequencing.

* Per Base Sequence Content
> This module will fail if the difference between A and T, or G and C is greater than 20% in any position. 

Is it ok?
