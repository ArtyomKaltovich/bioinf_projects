import anndata
import numpy as np
import scanpy as sc

data0 = r"/home/my/projects/bioinf_projects/project_7_rna/data/fermentation_0/counts_unfiltered/adata.h5ad"
data30 = r"/home/my/projects/bioinf_projects/project_7_rna/data/fermentation_30/counts_unfiltered/adata.h5ad"


def main():
    adata = anndata.read_h5ad(data30)
    print(adata)
    print(adata.var)


if __name__ == '__main__':
    main()
