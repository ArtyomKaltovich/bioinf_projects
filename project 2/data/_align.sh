#!/bin/sh
file=$1
suffix=.fastq.gz
name="${file%$postf}"

bwa mem reference.fasta $file | samtools view -S -b - | samtools sort -o $name.bam -
samtools index $name.bam "${name}_indexed.bam"
samtools mpileup -d 100000 -f reference.fasta "${name}_indexed.bam" > "${name}.mpileup"
java -jar ../../VarScan.v2.4.4.jar mpileup2snp "${name}.mpileup" --min-var-freq 0.001 --variants --output-vcf 1 > "${name}.vcf"
cat "${name}.vcf" | awk 'FNR==1{print "position,base,alt_base,frequency";next} NR>24 {split($10,a,":"); print $2, $4, $5, a[7]}' OFS=, > "${name}.csv"
