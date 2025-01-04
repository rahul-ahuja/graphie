# Graph presentation project

# 1. Folder Structure

```
├── data
│   ├── Data analysis.ipynb  
│   ├── reachability-meta.csv
│   ├── reachability.csv
│   ├── # Demonstration files
├── backend   
│   ├── serve.py            # serving the app on FastAPI
├── frontend   
│   ├── client.py           # user interface streamlit
├── graph_dir
│   ├── build_graph.py          # script to serialize graph
│   ├── calculate_shortest_path        # script to calculate shortest optimal path
│   ├── graph_igraph.pkl        # pickled graph
├── tests
│   ├── __init__.py
│   ├── conftest.py    # configuring the tests that is reading the data 
│   ├── test_data.py     # test to validate the data
├── Dockerfile         # To build the docker image
├── docker-compose.yml         # To build the docker image
├── requirements.txt   # packages to be installed
├── README.md          
├── environment.yml    # conda environment to setup the python environment
├── app.log            # logging the HTTP requests and response
└── .gitignore          # files to ignore during commits
```


# 2. Overview

This is Web interface to find the optimal path from the departature city to the destination using Djikstra Algorithm for path finding in the graph data. 

# 3. Setting up the project by conda

```
conda env create -f environment.yml
conda activate graphie
```


# 4. Run the App Serving from the project directory

``` 
uvicorn backend.serve:app --host 0.0.0.0 --port 8000 & streamlit run frontend/client.py --server.port 8501 --server.address 0.0.0.0
```
4ii. Go to the browser and put the URL address http://0.0.0.0:8501/ to access the Streamlit app

# 5. (Optionally) Run the app on the Docker. Docker enables us to run the app on any platform without requiring specific configuration

```
docker pull 785854/graphie-frontend:latest
docker pull 785854/graphie-backend:latest
docker-compose up
```

# 6. (Optional) To run the unit test on the data, 
```
pytest  #run on the main directory
```

# 7. Further work
`Raise a Github Issue for any issues`
