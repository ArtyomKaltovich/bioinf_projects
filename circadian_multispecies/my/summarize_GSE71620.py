import csv
from collections import defaultdict

import pandas as pd
import GEOparse as geo

CIRCADIAN_GENES = "ARNTL", "NR1D1", "PER3"  # 33297
FIELDS = "sample", "gene", "value"

path = "/run/media/my/New Volume/temp/GSE54650_family.soft.gz"
result = "data/GSE54650.csv"
#path = r"/run/media/my/New Volume/temp/GSE71620_family.soft.gz"
#result = "data/GSE71620.csv"

data = geo.get_GEO(filepath=path, silent=True)
pd.options.display.max_colwidth = 100000

circadian_genes_ids = defaultdict(list)
for gpl_name, gpl in data.gpls.items():
    print(gpl_name)
    df = gpl.table
    for gene in CIRCADIAN_GENES:
        d = df[df['gene_assignment'].str.upper().str.find(f"// {gene} //", end=40) != -1]
        print(d[["gene_assignment", "mrna_assignment"]])
        circadian_genes_ids[gene].extend(d["ID"])

print(circadian_genes_ids)

with open(result, "w") as result:
    result = csv.writer(result)
    result.writerow(FIELDS)

    for gsm_name, gsm in data.gsms.items():
        df = gsm.table
        for gene in CIRCADIAN_GENES:
            values = df[df["ID_REF"].isin(circadian_genes_ids[gene])]
            for v in values["VALUE"]:
                result.writerow((gsm_name, gene, v))
