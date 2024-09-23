import igraph

    # Load using igraph's pickle method
loaded_graph = igraph.Graph.Read_Pickle('graph_igraph.pkl')

def shortest_path(departature: str, destination: str, g: igraph = loaded_graph) -> tuple:
    source = g.vs.select(city_names_eq=departature)
    target = g.vs.select(city_names_eq=destination)
    shortest_path = g.get_shortest_paths(source[0], target[0], weights='travel_time')[0]
    short_path_rels = g.get_shortest_paths(source[0], target[0], weights='travel_time', output='epath')
    short_path_distances = [g.es[edge]['travel_time'] for edge in short_path_rels][0]
    shortest_travel_time = sum(short_path_distances)

    shortest_path_city = []
    for city_idx in range(len(shortest_path)):
        shortest_path_city.append(g.vs.select(city_ids_eq=shortest_path[city_idx])[0]['city_names'])




    return shortest_path_city, short_path_distances, shortest_travel_time

print(shortest_path('San Diego, CA', 'St. Johns, NL'))