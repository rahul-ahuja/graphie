from timeit import timeit
from calc_distances import get_distance

p1 = (45.4599, -98.4873)
p2 = (42.783, -73.339)

print("Profiling Python's get_distance function", timeit(lambda: get_distance(p1, p2), number=1000000))

from distance import get_distance # same function name conflict

print("Profiling C++ distance function", timeit(lambda: get_distance(p1, p2), number=1000000))