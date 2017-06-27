import os

import pandas as pd
import xarray as xr

BASE_URL = 'http://media.githubusercontent.com/media/olgabot/macosko2015/' \
           'master/macosko2015/data'


def read_csv(folder, filename):
    """Wrapper for pandas read_csv that uses the first column for the index"""
    return pd.read_csv(os.path.join(folder, filename), index_col=0)


def _load(prefix, subfolder, package):
    """Internal method for loading """
    folder = os.path.join(BASE_URL, subfolder)

    if package == 'xarray':
        return xr.open_dataset(os.path.join(folder, '{}.netcdf'.format(prefix)))
    if package == 'pandas':
        expression = read_csv(folder, '{}_expression.csv'.format(prefix))
        cell_metadata = read_csv(folder, '{}_cell_metadata.csv'.format(prefix))
        gene_metadata = read_csv(folder, '{}_gene_metadata.csv'.format(prefix))
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