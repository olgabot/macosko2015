import os

import pandas as pd
import xarray as xr

FOLDER = os.path.join(os.path.dirname(__file__))


def load_big_clusters(format='pandas'):
    """Read expression and metadata for 50 random cells from 6 biggest clusters
    
    Parameters
    ----------
    format : 'pandas' | 'xarray'

    Returns
    -------
    if format == "pandas":
        expression, cell_metadata, gene_metadata
    if format == "xarray"
    """
    folder = os.path.join(FOLDER, 'data',
                          '05_make_rentina_subsets_for_teaching')

    if format == 'xarray':
        return xr.open_dataset(os.path.join(folder, 'big_clusters.netcdf'))
    if format == 'pandas':
        expression = pd.read_csv(
            os.path.join(folder, 'big_clusters_expression.csv'))
        cell_metadata = pd.read_csv(
            os.path.join(folder, 'big_clusters_cell_metadata.csv'))
        gene_metadata = pd.read_csv(
            os.path.join(folder, 'big_clusters_gene_metadata.csv'))
        return expression, cell_metadata, gene_metadata
    else:
        raise ValueError('"{}" is not a valid format. Only "pandas" and '
                         '"xarray" are accepted'.format(format))

def load_amacrine(format='pandas'):
    """Read expression and metadata for 50 random cells from 6 biggest clusters
    
    Parameters
    ----------
    format : 'pandas' | 'xarray'

    Returns
    -------
    if format == "pandas":
        expression, cell_metadata, gene_metadata
    if format == "xarray"
    """
    folder = os.path.join(FOLDER, 'data',
                          '05_make_rentina_subsets_for_teaching')

    if format == 'xarray':
        return xr.open_dataset(os.path.join(folder, 'amacrine.netcdf'))
    if format == 'pandas':
        expression = pd.read_csv(
            os.path.join(folder, 'amacrine_expression.csv'))
        cell_metadata = pd.read_csv(
            os.path.join(folder, 'amacrine_cell_metadata.csv'))
        gene_metadata = pd.read_csv(
            os.path.join(folder, 'amacrine_gene_metadata.csv'))
        return expression, cell_metadata, gene_metadata
    else:
        raise ValueError('"{}" is not a valid format. Only "pandas" and '
                         '"xarray" are accepted'.format(format))