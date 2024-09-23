import pandas as pd
import igraph
import csv


df = pd.read_csv('../data/reachability-meta.csv')
node_ids = list(df['node_id'])
node_names = list(df['name'])


with open('../data/reachability.txt', 'r') as txt:
    reader = csv.reader(txt, delimiter=' ')
    edges = [edge for edge in reader][6:]
    edges = [[edge[0], edge[1], int(edge[2])*-1] for edge in edges]

edges_data = [[int(row[0]), int(row[1])] for row in edges]


g = igraph.Graph(directed=True) #initialize the empty graph

#populating the graph with nodes and relationships
g.add_vertices(len(node_ids)) #add nodes to the graph
g.add_edges(edges_data)

g.es['travel_time'] = [int(row[2]) for row in edges]
g.vs['city_names'] = node_names
g.vs['city_ids'] = node_ids


# Save using igraph's pickle method
g.write_pickle('graph_igraph.pkl')