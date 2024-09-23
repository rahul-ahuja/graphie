import igraph

    # Load using igraph's pickle method
loaded_graph = igraph.Graph.Read_Pickle('graph_igraph.pkl')

def shortest_path(departature: str, destination: str, g: igraph = loaded_graph):
    source = g.vs.select(city_names_eq=departature)
    target = g.vs.select(city_names_eq=destination)
    shortest_path = g.get_shortest_paths(source[0], target[0], weights='travel_time')
    short_path_rels = g.get_shortest_paths(source[0], target[0], weights='travel_time', output='epath')
    short_path_distances = [g.es[edge]['travel_time'] for edge in short_path_rels]
    shortest_travel_time = sum(short_path_distances[0])

    return shortest_path, short_path_distances, shortest_travel_time

print(shortest_path('San Diego, CA', 'St. Johns, NL'))