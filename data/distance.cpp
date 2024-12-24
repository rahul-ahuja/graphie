#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cmath>

constexpr double EARTH_RADIUS = 6371.0;

double get_distance(const std::pair<double, double>& p1, const std::pair<double, double>& p2) {
    double lat1 = p1.first, lon1 = p1.second;
    double lat2 = p2.first, lon2 = p2.second;

    double lat_dist = (lat2 - lat1) * M_PI / 180.0;
    double lon_dist = (lon2 - lon1) * M_PI / 180.0;

    double a = std::sin(lat_dist / 2) * std::sin(lat_dist / 2) +
               std::cos(lat1 * M_PI / 180.0) * std::cos(lat2 * M_PI / 180.0) *
               std::sin(lon_dist / 2) * std::sin(lon_dist / 2);

    double c = 2 * std::atan2(std::sqrt(a), std::sqrt(1 - a));
    return EARTH_RADIUS * c;
}

PYBIND11_MODULE(distance, m) {
    m.def("get_distance", &get_distance, "Calculate the distance between two points",
          pybind11::arg("p1"), pybind11::arg("p2"));
}
