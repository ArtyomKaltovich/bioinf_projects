import pandas as pd

RESULTS = r"C:\Users\artem\Downloads\Telegram Desktop\result.txt"


def main(path, level_of_significance):
    data = pd.read_csv(path, sep="\t").drop("Unnamed: 0", axis=1)
    print(f"{len(data)} genes at all")
    data = data[data["padj"] > level_of_significance]
    print(f"{len(data)} significant genes")
    regulation = data["log2FoldChange"] > 0
    up_regulated = sum(regulation)
    print(f"{up_regulated} up regulated")
    print(f"{len(regulation) - up_regulated} down regulated")


if __name__ == '__main__':
    main(RESULTS, level_of_significance=0.05)
