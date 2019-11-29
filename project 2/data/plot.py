import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def plot(name):
    print(name)
    plt.clf()
    data = pd.read_csv(name, index_col=False)
    print(data["frequency"].sort_values())
    data["frequency"].hist()
    name, _, _ = name.partition(".")
    plt.savefig(f"{name}.png")
    #info = data["frequency"].describe()
    #print(info)
    #print(data[(data["frequency"] < info["mean"] - 3 * info["std"]) |
    #           (data["frequency"] > info["mean"] + 3 * info["std"])])
    #return info["mean"], info["std"]


if __name__ == '__main__':
    info1 = plot("SRR1705858.fastq.gz.csv")
    info2 = plot("SRR1705859.fastq.gz.csv")
    info3 = plot("SRR1705860.fastq.gz.csv")
