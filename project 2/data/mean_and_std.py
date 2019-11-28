import pandas as pd
import numpy as np


def mean_and_str(name):
    print(name)
    data = pd.read_csv(name, index_col=False)
    info = data["frequency"].describe()
    print(info)
    print(data[(data["frequency"] < info["mean"] - 3 * info["std"]) |
               (data["frequency"] > info["mean"] + 3 * info["std"])])
    return info["mean"], info["std"]


def process_roommate(path, mean, std):
    data = pd.read_csv(path, index_col=False)
    print(data[(data["frequency"] < mean - 3 * std) |
               (data["frequency"] > mean + 3 * std)])


if __name__ == '__main__':
    info1 = mean_and_str("SRR1705858.fastq.gz.csv")
    info2 = mean_and_str("SRR1705859.fastq.gz.csv")
    info3 = mean_and_str("SRR1705860.fastq.gz.csv")
    info = np.mean((info1[0], info2[0], info3[0])),\
           max(info1[1], info2[1], info3[1])
    print(info)

    process_roommate("roommate_0.001.csv", *info)
