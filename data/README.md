# Demonstrating the performance gains of the codes

### Assess the speed of the Python get_distance and C++ distance functions by running the below;

```
python setup.py build_ext --inplace
python profile_script.py
```

Profiling Python's get_distance function 0.801099723000334
Profiling C++ distance function 0.27820833899977515