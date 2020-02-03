import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

CIRCADIAN_GENES = "ARNTL", "NR1D1", "PER3"

data = pd.read_csv("data/GSE39445.csv")
for gene in CIRCADIAN_GENES:
    data[gene] /= data["PUF60"]
extension = data[data["sleepprotocol"] == "Sleep Extension"]
restriction = data[data["sleepprotocol"] == "Sleep Restriction"]
fig, ax = plt.subplots(1, 3)
for i, gene in enumerate(CIRCADIAN_GENES):
    sns.regplot("circadianphase", gene, data=extension, x_estimator=np.mean, order=3, ax=ax[i])
plt.show()
