* 23.02.2020 - download data
* 24.02.2020 - trying to install repeatmodeler

    $ yaourt -S anaconda

fails as there are not free space, clean it and using python-conda

    $ yaourt -S python-conda
    
fails. Updating them with pip gave nothing.
The reason was yaourt can't overwrite files created by pip. Google suggest 
using --overwrite flag

    $ yaourt -S python-conda --overwrite paths
    $ yaourt --overwrite paths -S python-conda
    $ yaourt -S --overwrite paths python-conda

all failed.

    $ yaourt -S python-conda --force
    
works!

    $ conda install -c bioconda repeatmodeler

fails as no conda environment. Create it, trying to activate it fails due to
lack of user writes and config files. When I was trying to fix it - sudo was 
broken due to recursive chmod. Fixing it with logout/login by the way 
ctrl+alt+f1 doesn't work as expected in arch linux.

That's all, folks!

* 25.02.2020 - still trying to install repeatmodeler
 
- removing python-conda and install miniconda3 it fails with
        
        
    Traceback (most recent call last):
      File "/usr/condabin/conda", line 12, in <module>
        from conda.cli import main
          ModuleNotFoundError: No module named 'conda'

- installing conda with pip, it still fails
- the problem was with command suggested by conda
    
    
    $ sudo ln -s /opt/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh

- the one should use
    
    
    $ echo "[ -f /opt/miniconda3/etc/profile.d/conda.sh ] && source /opt/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    
- It's alive! But still does work, as can't satisfy dependencies
    
- creating new conda's environment
- still fails
- updating python packages with 
    
    
    $ sudo pip install -U $(pip freeze | awk '{split($0, a, "=="); print a[1]}')
    ERROR: Cannot uninstall 'pep517'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
    
- fixed with
    
    
    $ sudo pip install --ignore-installed pep517
    
- still fails
    
    
    Collecting xgboost
      Using cached xgboost-1.0.1-py3-none-manylinux1_x86_64.whl (109.7 MB)
    ERROR: Could not find a version that satisfies the requirement zippD (from versions: none)
    ERROR: No matching distribution found for zippD
    
    $ sudo pip uninstall xgboost

- still failing
    
    $ sudo pip install zipp
    
fails with
     
        ERROR: Could not find a version that satisfies the requirement urllib3D (from versions: none)
        ERROR: No matching distribution found for urllib3D
       
* 26.02.2020 - still trying to install repeatmodeler

- trying on virtual machines - both failed
- trying to install directly by unpacking tar archive from official site - failed as no perl packages

* 27.02.2020 - still trying to install repeatmodeler

- cpan failed to install them    
- installing with pacman
- repeatmodeler needs repeatmasker
- conda installation failed
- installing it from aur - yaourt is deprecated
- installing yay - package is outdated
- changing pckbuild - fails on integrity check
- disable integrity check
    
    
    install: cannot stat 'license.txt': No such file or directory
    ==> ERROR: A failure occurred in package()

- editing pkgbuild - installation stuck

Olya: I installed program via Anaconda.
I got error during first step - building database.
/home/olya/anaconda3/share/RepeatModeler/BuildDatabase -name waterbear GCA_001949185.fa

Empty compile time value given to use lib at /home/olya/anaconda3/share/RepeatModeler/BuildDatabase line 121.
Building database waterbear:
  Reading GCA_001949185.fa...
The makeblastdb program did not generate the
file waterbear.nsq.  Please check your input file(s) for potential formating errors.
/makeblastdb returned:
The command used was: /makeblastdb -blastdb_version 4 -out waterbear -parse_seqids -dbtype nucl -in ./WYCtMExWnM 2>&1
Died at /home/olya/anaconda3/share/RepeatModeler/BuildDatabase line 333.

I glimpsed on perl code and found out that there are some problems with makeblastdb program inside code. Temp file WYCtMExWnM was created, I used it in comand
makeblastdb -blastdb_version 4 -out waterbear -parse_seqids -dbtype nucl -in WYCtMExWnM 2>&1

it worked!
Building a new DB, current time: 02/27/2020 01:47:00
New DB name:   /home/olya/Documents/BIproject4/waterbear
New DB title:  WYCtMExWnM
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 200 sequences in 0.59969 seconds.
3. Run RepeatModeler
a run using 20 parallel jobs

but it was too early to feel happy

It took near 6 hours to run the next step. And it is impossible for me to understand reasons of killing the process.
error durig second round - отчаяние 
Sampling Time: 00:00:49 (hh:mm:ss) Elapsed Time
Running all-by-other comparisons...
/home/olya/anaconda3/bin/RepeatModeler: line 17:  3781 Killed                  perl /home/olya/anaconda3/share/RepeatModeler/${NAME} $@
 
second try nohup RepeatModeler -database /home/olya/Documents/BIproject4/waterbear > run.out &
not very effective too

* 28.02.2020
2. predict coding regions in the genome

Augustus web version was used
http://bioinf.uni-greifswald.de/webaugustus/prediction/show/0db58ea1706765a901707ed7bac0001a
We have Prediction archive  predictions.tar.gz, but we got it after making next steps of the project. It was too late.

3. (Optional) Model training
We skipped this step, because we wanted to complete the project before deadline and Augustus output came too late.

4. Intro -  Functional annotation.

We downloaded AUGUSTUS results here.
We extracted protein sequences (fasta) from the prediction output.
perl getAnnoFasta.pl augustus.whole.gff

We have 16435 protein sequences in our dataset.

Count the number of obtained proteins (e.g. grep all the strings with “>” symbol and count lines with wc -l).
grep '>' augustus.whole.aa | wc -l
16435

5. Physical localization 
we may hypothesize that tardigrades might have unique proteins associated with their DNA to protect and/or effectively repair it
Our collegues sent us a list of peptides that were associated with the DNA
our goal is to figure out which proteins from the R. varieornatus genome these peptides correspond to

We did  local blast search: 1. created local database from protein fasta file with makeblastdb
making database
makeblastdb -in augustus.whole.aa -parse_seqids -blastdb_version 5 -title "waterbear peptides" -dbtype prot

2. blastp using peptide sequence file as a query
blastp -db /home/olya/Documents/BIproject4/augustus.whole.aa -query peptides.fa -out blastresults -outfmt 6

Extraction proteins of interest from initial file
cut -f 2 blastresults > matches.txt -blastp hits
xargs samtools faidx augustus.whole.aa <matches.txt >> proteins_of_interest.fasta - making multifasta file 

проверить на уникальность, вроде там есть повторяющиеся
6. Localization prediction
 We used  WoLF PSORT  and  TargetP 1.1 tools to predict the subcellular localization of proteins
TargetP 1.1  output

7. BLAST search

 We BLASTed protein sequences against “UniProtKB/Swiss-Prot” database/

We downloaded  swissprot database:
 update_blastdb.pl --decompress swissprot
 
blasting:
blastp -db swissprot -query proteins_of_interest.fasta -out blastresults7step -outfmt 6

,save in your journal the Accession Number, E-value, % Ident, % Query coverage, and annotation.

интерпретация 
E value: The E value (expected value) is a number that describes how many times you 
would expect a match by chance in a database of that size. The lower the E value is, 
the more significant the match.
Percent Identity: The percent identity is a number that describes how similar the query 
sequence is to the target sequence (how many characters in each sequence are 
identical). The higher the percent identity is, the more significant the match.
Query Cover: The query cover is a number that describes how much of the query 
sequence is covered by the target sequence. If the target sequence in the database 
spans the whole query sequence, then the query cover is 100%. This tells us how long 
the sequences are, relative to each other.

8. Pfam prediction

https://www.ebi.ac.uk/Tools/hmmer/
We searched our protein sequences against a collection of profile-HMMs for different protein domains and motifs (pfam database).

output:
 https://www.ebi.ac.uk/Tools/hmmer/results/90350804-59A2-11EA-899E-10AFF75AEC3D/score

- create the script for parse wolfpsort output - parse_wolfpsort.py
- put its output to data/details_urls.csv
- create the script for parse hmmer output - parse_hmmer.py
- put its output to data/hmmer_data.csv
