# Graph presentation project

# 1. Folder Structure

```
├── data
│   ├── Data analysis.ipynb  
│   ├── reachability-meta.csv
│   ├── reachability.csv   
├── graph_dir
│   ├── build_graph.py          # script to serialize graph
│   ├── calculate_shortest_path        # script to calculate shortest optimal path
│   ├── graph_igraph.pkl        # pickled graph
├── tests
│   ├── __init__.py
│   ├── conftest.py    # configuring the tests that is reading the data 
│   ├── test_data.py     # test to validate the data
├── Dockerfile         # To build the docker image
├── app.log            # logging the HTTP requests and response
├── server.py          # serving the app on FastAPI
├── requirements.txt   # packages to be installed
├── README.md          
├── environment.yml    # conda environment to setup the python environment
└── .gitignore          # files to ignore during commits
```


# 2. Overview

This is Web interface to find the optimal path from the departature city to the destination using Djikstra Algorithm for path finding in the graph data. 

# 3. Setting up the project by conda

```
conda env create -f environment.yml
conda activate graph_durham
```


# 4. Run the App Serving

``` 
uvicorn serve:app
```

# 5. (Optionally) Run the app on the Docker. Docker enables us to run the app on any platform without requiring specific configuration

```
docker pull 785854/graphie:latest
docker run -d --name mlapp -p 8000:8000 785854/graphie:latest
```

# 6. Test the FastAPI on the localhost with port number as below; This will direct you to the Swagger UI for the API testing

```
http://127.0.0.1:8000/docs

Example cities;
"San Diego, CA"
"St. Johns, NL"
"Washington, DC"
```

# 7. (Optional) To run the unit test on the data, 
```
pytest  #run on the main directory
```

# 8. Further work
`Raise a Github Issue for any issues`
