import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

CIRCADIAN_GENES = "ARNTL", "NR1D1", "PER3"

data = pd.read_csv("data/GSE71620.csv").dropna()  # GSE54650
fig, ax = plt.subplots(1, 3)
for i, gene in enumerate(CIRCADIAN_GENES):
    gene_data = data[data["gene"] == gene]
    values = list(gene_data["value"])
    times = list(gene_data["tod"])   # ct for GSE54650
    sns.regplot(times, values, x_estimator=np.mean, order=3, ax=ax[i], marker="x")
    ax[i].set_title(gene)
plt.show()
