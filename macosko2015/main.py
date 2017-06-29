import pandas as pd
import xarray as xr

try:
    # Python 2
    from urlparse import urljoin
except ImportError:
    # Python 3
    from urllib.parse import urljoin

BASE_URL = "https://media.githubusercontent.com/media/olgabot/macosko2015/" \
         "master/data/"


def read_csv(folder, filename):
    """Wrapper for pandas read_csv that uses the first column for the index"""
    csv = urljoin(folder, filename)
    return pd.read_csv(csv, index_col=0)


def _load(prefix, subfolder, package):
    """Internal method for loading """

    # Add terminal slash because urljoin is not smart
    subfolder = subfolder + '/' if not subfolder.endswith('/') else subfolder

    folder = urljoin(BASE_URL, subfolder)

    expression = read_csv(folder, '{}_expression.csv'.format(prefix))
    cell_metadata = read_csv(folder, '{}_cell_metadata.csv'.format(prefix))
    gene_metadata = read_csv(folder, '{}_gene_metadata.csv'.format(prefix))

    if package == 'xarray':
        ds = xr.Dataset({'expression': (['cell', 'gene'], expression),
                         'gene_metadata':
                             (['gene', 'gene_feature', ], gene_metadata),
                         'cell_metadata':
                             (['cell', 'cell_feature'], cell_metadata)},
                        coords={'gene': expression.columns,
                                'cell': expression.index})
        return ds
    if package == 'pandas':
        return expression, cell_metadata, gene_metadata
    else:
        raise ValueError('"{}" is not a valid format. Only "pandas" and '
                         '"xarray" are accepted'.format(package))


def load_big_clusters(package='pandas'):
    """Read expression and metadata for 50 random cells from 6 biggest clusters
    
    Parameters
    ----------
    package : 'pandas' | 'xarray'

    Returns
    -------
    if format == "pandas":
        expression, cell_metadata, gene_metadata
    if format == "xarray"
    """
    return _load('big_clusters', '05_make_rentina_subsets_for_teaching',
                 package)


def load_amacrine(package='pandas'):
    """Read expression and metadata for 50 random cells from 6 biggest clusters
    
    Parameters
    ----------
    package : 'pandas' | 'xarray'

    Returns
    -------
    if format == "pandas":
        expression, cell_metadata, gene_metadata
    if format == "xarray"
    """
    return _load('amacrine', '05_make_rentina_subsets_for_teaching',
                 package)
