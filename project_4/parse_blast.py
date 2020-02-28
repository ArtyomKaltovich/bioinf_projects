import pandas as pd

BLAST_FILE = r"data/blastresults7step"
# 1.    qseqid    query (e.g., gene) sequence id
#  2.    sseqid    subject (e.g., reference genome) sequence id
#  3.    pident    percentage of identical matches
#  4.    length    alignment length
#  5.    mismatch    number of mismatches
#  6.    gapopen    number of gap openings
#  7.    qstart    start of alignment in query
#  8.    qend    end of alignment in query
#  9.    sstart    start of alignment in subject
#  10.    send    end of alignment in subject
#  11.    evalue    expect value
#  12.    bitscore    bit score
BLAST_COLUMNS = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore"]
RESULTED_FILE = r"data\blast_best.csv"
ESCORE_THRESHOLD = 10 ** -10

if __name__ == '__main__':
    df = pd.read_csv(BLAST_FILE, names=BLAST_COLUMNS, sep="\t")
    idx = df.groupby(['qseqid'], sort=False)['evalue'].transform(min) == df['evalue']
    df = df[idx]
    df = df[df["evalue"] < ESCORE_THRESHOLD]
    df.to_csv(RESULTED_FILE)
