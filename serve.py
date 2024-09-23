from fastapi import FastAPI, Query, HTTPException
import uvicorn
import pandas as pd
import igraph
from neo4j import GraphDatabase
from pydantic import BaseModel, Field
from graph_dir.calculate_shortest_path import shortest_path

import logging

# Configure logging
logging.basicConfig(filename="app.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = FastAPI(
    title="Travel Agent API",
    description="API to test Graph travel model",
    version="1.0.0"
)

# Load using igraph's pickle method
loaded_graph = igraph.Graph.Read_Pickle('graph_dir/graph_igraph.pkl')


# Define the input data schema
class City(BaseModel):
    source_city_name: str = Field(description="The name of the city")
    target_city_name: str = Field(description="The name of the city")


# Define the response schema
class RecommendationResponse(BaseModel):
    optimal_path: str = Field(description="Gives out the optimal path with cities and time")


# FastAPI lifecycle events
# Global Neo4j driver
driver = None

@app.on_event("startup")
def startup():
    global driver
    # Initialize the Neo4j driver
    driver = GraphDatabase.driver(uri='bolt://localhost:7687', auth=('neo4j', 'password'))

@app.on_event("shutdown")
def shutdown():
    if driver:
        driver.close()  # Close the Neo4j connection gracefully

@app.post('/path', response_model=RecommendationResponse, tags=["Recommendation endpoint"])
async def travel(city: City):
    """
    Endpoint for getting the optimal travel path \n
    Enter in the Request body the names of the departure city and destination city
    """

    logger.info(f"Received travel request from {city.source_city_name} to {city.target_city_name}")



        # Cypher query to check if both cities exist
    check_cities_cypher = '''
        MATCH (source:City {name: $city.source_city_name}), (target:City {name: $target_name})
        RETURN source, target
    '''

    #HTTP Exception error handling raise HTTPException(status_code=404, detail="One or both cities not found in the database.")
    
    city_path, path_distances, travel_time = shortest_path(departature = "Abbotsford, BC", destination = "Akron/Canton, OH", g = loaded_graph)
    
    #pydantic output response
    response = {"optimal_path": str(city_path)} 

    return response





if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)