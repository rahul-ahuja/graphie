import igraph
import pytest
import pandas as pd

#The fixture is created once per module that uses it and is destroyed at the end of the test session.
@pytest.fixture(scope="module")
def pickled_graph():
    return igraph.Graph.Read_Pickle('graph_dir/graph_igraph.pkl')

#destroyed at the end of the function call
@pytest.fixture(scope="function")
def nodes_df():
    return pd.read_csv('data/reachability-meta.csv')

#destroyed at the end of the function call
@pytest.fixture(scope="function")
def edges_df():
    return pd.read_csv('data/reachability.csv', header=None)
