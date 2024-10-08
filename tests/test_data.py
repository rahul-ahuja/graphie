import pandas as pd


def test_num_nodes(pickled_graph, nodes_df):
    "Match the number of rows in the dataframe with node attributes and the number of nodes in the graphs"
    assert len(pickled_graph.vs) == len(nodes_df)


def test_num_edges(pickled_graph, edges_df):
    "Match the number of rows in the dataframes with edges and the number of edges in the graphs"
    assert len(pickled_graph.es) == len(edges_df)


def test_check_node_entry(pickled_graph, nodes_df):
    "Match entries in the graph and the dataframe"
    city_name = "Los Angeles, CA"
    city_id_graph = pickled_graph.vs.select(city_names_eq=city_name)[0]['city_ids']
    city_id_df = nodes_df[nodes_df['name'] == city_name]['node_id'].values[0]
    assert city_id_graph == city_id_df
