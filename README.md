# macosko2015

Expression data for Macosko et al, "Highly Parallel Genome-wide Expression Profiling of Individual Cells Using Nanoliter Droplets," Cell (2015)

This repo aggregates:
- Text files (`.txt.gz`) files downloaded from the GEO Accession: [GSE63473](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63473)
- Supplementary data/excel files from the [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4481139/)
- Cluster identities from the [Drop-Seq website](http://mccarrolllab.com/dropseq/)

## How to install

Due to space limitations on the Python Package Index (PyPI), estimated at 60MB,
the best way to install this repo is to call `pip` on this GitHub repository:

```
pip install git+git://github.com/olgabot/macosko2015.git
```

If you want to clone the repository and install it, then to avoid copying the
files around and having the data take up too much space, it's best to install
in "editable mode" (`-e`) as that will simply point your current Python to this directory:

```
git clone git@github.com:olgabot/macosko2015
cd macosko2015
pip install -e .
```

## Repo organization


Within the package folder `macosko2015`, this repo consists of 2 major folders,
`data` and `notebooks`. They mirror each other in structure, so everything in
`data` can be tracked to a specific notebook.

Currently, the `data` folder consists of 6 folders:

```
macosko2015/
└── data
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
macosko2015/
└── notebooks
    ├── 02_make_celltype_metadata.ipynb
    ├── 03_clean_cluster_assignments.ipynb
    ├── 04_extract_data_from_supplementary_excel_files.ipynb
    ├── 05_make_rentina_subsets_for_teaching.ipynb
    ├── 06_combine_retina_data.ipynb
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
access it, use the built-in function `load_big_clusters`. By default, this
outputs three pandas dataframes:

- `expression` matrix of raw digital expression counts (unique molecular
  identifier/UMI counts)
- `cells` metadata, indicating which cluster each cell was assigned to in the paper
- `genes` metadata, indicating which cluster differentially expressed this gene

Note: this downloads a file from GitHub and thus requires an internet
connection.

```python
import macosko2015

expression, cells, genes = macosko2015.load_big_clusters()
```

Or if you like using `xarray`](http://xarray.pydata.org/), you can specify to
use the `xarray` package:


```python
import macosko2015

big_clusters = macosko2015.load_big_clusters('xarray')
```

### Mini-dataset 2: Amacrine cells, batch 1

This dataset consists of all amacrine cells (clusters 3-23, inclusive) from the
first run (batch).

Note: this downloads a file from GitHub and thus requires an internet
connection.

```python
import macosko2015

expression, cells, genes = macosko2015.load_amacrine()
```


Or use [`xarray`](http://xarray.pydata.org/) to access the NetCDF dataset:

```python
import macosko2015

amacrine = macosko2015.load_amacrine('amacrine')
```
### Larger datasest

Beyond the datasets above, even a single batch's digital expression matrix is
too big for PyPI or GitHub, and is tracked by GitHub's Large File Storage (LFS)
. If you want access to the all of the data, it is best to `git clone` the repo
and fetch all the data stored on `git lfs`. If you haven't already, you will
need [install `git lfs`](https://help.github.com/articles/installing-git-large-file-storage/.

With SSH keys:

```git
git clone git@github.com:olgabot/macosko2015
git lfs fetch
```
Over HTTP:
```git
git clone https://github.com/olgabot/macosko2015
git lfs fetch
```

## Jupyter Notebooks of Data Cleaning

If you are interested in learning how the data was cleaned and unified into
this format, the best way to get this information is by cloning this repository
and exploring the notebooks in the subfolder `macosko2015/notebooks`.

## Contributions

Contributions, especially to improving the cleaning of the datasets, are welcome!

## License

The code is distributed under a MIT license.