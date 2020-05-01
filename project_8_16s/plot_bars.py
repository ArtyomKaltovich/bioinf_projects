import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BAR_DATA = r"data/output.txt"


def main(path):
    data = pd.read_csv(path, sep="\t", names=["name", "proc"], skiprows=1)
    data["level"] = data["name"].str.count("\|")  # \ was added because count accept regexes
    for i in data["level"].unique():
        if i:
            d = data[data["level"] == i]
            xs = d["name"].str.rpartition("|")[2]
            ys = d["proc"]
            sns.barplot(xs, ys)
            plt.xlabel("Taxa")
            plt.ylabel("Percent")
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.savefig(f"plot/taxa_bar_level_{i}.png")
            plt.clf()


if __name__ == '__main__':
    main(BAR_DATA)
