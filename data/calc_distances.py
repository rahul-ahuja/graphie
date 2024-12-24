import math
import pandas as pd

def get_distance(p1, p2):
    lat1, lon1 = p1
    lat2, lon2 = p2
 
    lat_dist = math.radians(lat2 - lat1)
    lon_dist = math.radians(lon2 - lon1)
    a = (
        math.sin(lat_dist / 2) * math.sin(lat_dist / 2) +
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
        math.sin(lon_dist / 2) * math.sin(lon_dist / 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    earth_radius = 6371
    dist = earth_radius * c
 
    return dist
 
 
def get_distances(stations, locations):

    distances = {}
    for first_i in range(len(stations) - 1): 
        first_station = stations[first_i]           
        first_location = locations[first_station]
        for second_i in range(first_i, len(stations)):  
            second_station = stations[second_i]
            second_location = locations[second_station]
            distances[(first_station, second_station)] = get_distance(
                first_location, second_location)
    return distances
 
 
def get_locations():
    df = pd.read_csv('reachability-meta.csv', usecols=['name', 'latitude', 'longitude'])
    for row in df.iterrows():
        station, (lat, lon)  = row[1].values[0], (row[1].values[1], row[1].values[2]) 
        yield station, (lat, lon)


#locations = {station: (lat, lon) for station, (lat, lon) in get_locations()}
#stations = sorted(locations.keys())
#distances = get_distances(stations, locations)

# In the get_distances function, comparing all the stations between each other, the complexity is of the order n2.

#Code that calls out to external libraries (such as regular expressions, string operations, and calls to database libraries) is unlikely to show any speedup after compiling. Programs that are I/O-bound are also unlikely to show significant speedups.

#The tools we’ll look at split roughly into two sets: tools for compiling ahead of time, or AOT (Cython), and tools for compiling “just in time,” or JIT (Numba, PyPy).

#Adding primitive C types to start making our compiled function run faster by doing more work in C and less via the Python virtual machine