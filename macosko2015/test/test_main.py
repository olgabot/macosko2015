import pandas as pd
import pytest
import xarray as xr


@pytest.fixture(params=['pandas', 'xarray'])
def package(request):
    return request.param

@pytest.fixture(params=['big_clusters', 'amacrine'])
def name(request):
    return request.param


def test_load_data(package, name):
    from macosko2015 import load_amacrine, load_big_clusters

    returned = eval('load_{name}("{package}")'.format(
        package=package, name=name))

    if package == 'pandas':
        assert len(returned) == 3
        for x in returned:
            assert isinstance(x, pd.DataFrame)

        # Make sure the axes of expression data and the cell/gene metadata
        # match up
        expr, cells, genes = returned
        assert len(expr.index) == len(cells.index)
        assert len(expr.columns) == len(genes.index)
    elif package == "xarray":
        assert isinstance(returned, xr.Dataset)

        # Don't need to check that axes line up because xarray does that for us
