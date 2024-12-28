import igraph
import pytest
import pandas as pd

#If the scope is module then the fixture is created once per module that uses it and is destroyed at the end of the test session.
#If the scope is function then the fixture is destroyed at the end of the function call

@pytest.fixture(scope="module")
def pickled_graph():
    return igraph.Graph.Read_Pickle('graph_dir/graph_igraph.pkl')

@pytest.fixture(scope="module")
def nodes_df():
    return pd.read_csv('data/reachability-meta.csv')

@pytest.fixture(scope="module")
def edges_df():
    return pd.read_csv('data/reachability.csv', header=None)
