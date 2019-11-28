from functools import partial

import pandas as pd


if __name__ == '__main__':
    info1 = pd.read_csv("SRR1705858.fastq.gz.csv")
    info2 = pd.read_csv("SRR1705859.fastq.gz.csv")
    info3 = pd.read_csv("SRR1705860.fastq.gz.csv")
    repeated_positions = sorted(set(info1["position"]) & set(info2["position"]) & set(info3["position"]))
    print(info1[info1["position"].isin(repeated_positions)])
