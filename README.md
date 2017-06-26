# macosko2015

Expression data for Macosko et al, "Highly Parallel Genome-wide Expression Profiling of Individual Cells Using Nanoliter Droplets," Cell (2015)

This repo aggregates:
- Text files (`.txt.gz`) files downloaded from the GEO Accession: [GSE63473](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63473)
- Supplementary data/excel files from the [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)
- Cluster identities from the [Drop-Seq website](http://mccarrolllab.com/dropseq/)

## Repo organization


This repo consists of 2 major folders, `data` and `notebooks`. They mirror each
other in structure, so everything in `data` can be tracked to a specific notebook.

Currently, the `data` folder consists of 6 folders:

```
data
├── 00_original/
├── 02_make_celltype_metadata/
├── 03_clean_cluster_assignments/
├── 04_extract_data_from_supplementary_excel_files/
├── 05_combine_retina_data/
└── 05_make_rentina_subsets_for_teaching/
```

Except for `00_original`, the contents of each folder can be traced back to an
exact notebook:

```
notebooks
├── 02_make_celltype_metadata.ipynb
├── 03_clean_cluster_assignments.ipynb
├── 04_extract_data_from_supplementary_excel_files.ipynb
├── 05_make_rentina_subsets_for_teaching.ipynb
├── 06_combine_retina_data.ipynb
├── __pycache__
└── common.py
```

Finally, `common.py` consists of code that is shared between all the notebooks,
especially boilerplate code defining the locations of the folders.

If you're wondering why there isn't a `01_...` notebook, that's because
originally, there was ONE `01_data_cleaning` notebook before I realized it was
a much bigger job that required more than one notebook :)

## Data files

So far, only the retina data (figures 4-6) has been aggregated. The HEK293T
(human) and 3T3 (mouse) cell line data has not been cleaned or aggregated (but
if you clean them, consider contributing to this repo!), though the mouse cell
cycle genes *have* been added to the gene metadata.

The mini-datasets were created in
[`notebooks/05_make_rentina_subsets_for_teaching.ipynb`](notebooks/05_make_rentina_subsets_for_teaching.ipynb)

### Mini-dataset 1: 50 cells from 6 clusters, batch 1

This dataset consists of 50 random cells from the six largest clusters
(clusters 24, 25, 26, 27, 33, 34) from the first run (batch). This is a useful
benchmarking dataset for testing things like clustering, gene dropout. To
access it, you can extract each of the files individually:

```python
import os

import pandas as pd

folder = os.path.join('data', '05_make_rentina_subsets_for_teaching')
expression = pd.read_csv(os.path.join(folder, 'big_clusters_expression.csv'))
cell_metadata = pd.read_csv(os.path.join(folder, 'big_clusters_cell_metadata.csv'))
gene_metadata = pd.read_csv(os.path.join(folder, 'big_clusters_gene_metadata.csv'))
```


Or use [`xarray`](http://xarray.pydata.org/) to access the NetCDF dataset:

```python
import os

import xarray as xr

folder = os.path.join('data', '05_make_rentina_subsets_for_teaching')
filename = os.path.join(folder, 'big_clusters.netcdf')
ds = xr.open_dataset(filename)
```

### Mini-dataset 2: Amacrine cells, batch 1

This dataset consists of all amacrine cells (clusters 3-23, inclusive) from the
first run (batch).

```python
import os

import pandas as pd

folder = os.path.join('data', '05_make_rentina_subsets_for_teaching')
expression = pd.read_csv(os.path.join(folder, 'amacrine_expression.csv'))
cell_metadata = pd.read_csv(os.path.join(folder, 'amacrine_cell_metadata.csv'))
gene_metadata = pd.read_csv(os.path.join(folder, 'amacrine_gene_metadata.csv'))
```


Or use [`xarray`](http://xarray.pydata.org/) to access the NetCDF dataset:

```python
import os

import xarray as xr

folder = os.path.join('data', '05_make_rentina_subsets_for_teaching')
filename = os.path.join(folder, 'amacrine.netcdf')
ds = xr.open_dataset(filename)
```


## Contributions

Contributions, especially to improving the cleaning of the datasets, are welcome!

## License

The code is distributed under a MIT license.