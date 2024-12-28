import pandas as pd
from graph_dir.calculate_shortest_path import shortest_path

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

def test_min_distance(edges_df, pickled_graph):
    "Match the minimum time from the dataframes with the shortest time from the shortest path function"
    min_time = min(edges_df[2])
    depart_id, dest_id = edges_df[edges_df[2] == min(edges_df[2])][0].values
    depart_name = pickled_graph.vs.select(city_ids_eq=depart_id)[0]['city_names']
    dest_name = pickled_graph.vs.select(city_ids_eq=dest_id)[0]['city_names']
    shortest_time = shortest_path(depart_name, dest_name, pickled_graph)[-1]
    assert shortest_time == min_time