import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("data/GSE39445.csv")
extension = data[data["sleepprotocol"] == "Sleep Extension"]
restriction = data[data["sleepprotocol"] == "Sleep Restriction"]
sns.regplot("hoursawake", "NR1D1", restriction, x_estimator=np.mean)
#sns.scatterplot("circadianphase", "NR1D1", data=restriction)
plt.show()
