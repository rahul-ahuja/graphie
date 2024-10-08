from fastapi import FastAPI, Query, HTTPException
import uvicorn
import pandas as pd
import igraph
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



@app.post('/path', response_model=RecommendationResponse, tags=["Recommendation endpoint"])
def travel(city: City):
    """
    Endpoint for getting the optimal travel path \n
    Enter in the Request body the names of the departure city and destination city
    """

    logger.info(f"Received travel request from {city.source_city_name} to {city.target_city_name}")



        # query to check if both cities exist
    try:
        loaded_graph.vs.select(city_names_eq=city.source_city_name)[0] 
        loaded_graph.vs.select(city_names_eq=city.target_city_name)[0]
    except IndexError:     #HTTP Exception error handling 
        raise HTTPException(status_code=404, detail="One or both cities not found in the graph.")


    
    city_path, path_travel_time, total_travel_time = shortest_path(departature = city.source_city_name, destination = city.target_city_name, g = loaded_graph)
    
    path_description = ""
    source_city = city_path[0]
    for city, travel_time in zip(city_path[1:], path_travel_time):
        path_description += f"It takes {travel_time} mins from {source_city} to {city} \n    "
        source_city = city 

    logger.info(f"API outputs {path_description}")

    path_description += f"Total journey time will be {total_travel_time} mins."

    #pydantic output response
    response = {"optimal_path": path_description} 

    return response


if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)