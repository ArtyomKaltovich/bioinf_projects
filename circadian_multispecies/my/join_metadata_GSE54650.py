import pandas as pd

metadata = pd.read_csv("data/GSE54650_metadata.csv", names=["sample", "name"], sep="\t")
metadata[["tissue", "ct"]] = metadata["name"].str.split("_", expand=True)
metadata = metadata[metadata["tissue"].isin(["Hyp"])]
metadata["sample"] = metadata["sample"].str.strip()
metadata["ct"] = metadata["ct"].str[2:].astype(int) % 24
data = pd.read_csv("data/GSE54650.csv")
result = pd.merge(data, metadata, on="sample")
result.to_csv("data/GSE54650.csv")
