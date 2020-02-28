import pandas as pd

BEST_BLAST_DATA = r"data/blast_best.csv"
HMMER_DATA = r"data/hmmer_data.csv"
WOLFPSORT_DATA = r"data/details_urls.csv"
RESULT_PATH = r"data/result.tsv"


if __name__ == '__main__':
    data = pd.read_csv(BEST_BLAST_DATA)
    hmmer = pd.read_csv(HMMER_DATA)
    hmmer["qseqid"] = hmmer["query_name"]
    data = pd.merge(data, hmmer, on="qseqid")
    data.drop(["Unnamed: 0_x", "Unnamed: 0_y", "query_name"], inplace=True, axis=1)

    wolf = pd.read_csv(WOLFPSORT_DATA)
    wolf.rename(dict(id="qseqid"), inplace=True, axis=1)
    data = pd.merge(data, wolf, on="qseqid")
    data.to_csv(RESULT_PATH, sep="\t")
