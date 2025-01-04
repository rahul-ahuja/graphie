import streamlit as st
import json
import requests
import pandas as pd
import os
import sys

@st.cache_data
def load_cities(path: str) -> tuple:
    city_list = pd.read_csv(path, usecols=["name"])
    city_tuples = (tuple(city_list['name'].tolist()))
    return city_tuples

city_tuples = load_cities('data/reachability-meta.csv')

st.title("Travel Agent: Finding the optimal path")

departure_city = st.selectbox('Departing City',
                              city_tuples)


destination_city = st.selectbox('Destination City',
                              city_tuples)


#converting the inputs into a json format
city = {'source_city_name': departure_city, 'target_city_name': destination_city}

#when the user clicks on button it will fetch the API
if st.button('Calculate'):
    response = requests.post(url="http://0.0.0.0:8000/path", data= json.dumps(city))
    # Extract the optimal path
    #optimal_path = response

    optimal_path = eval(response.text.replace("'", "\""))
    path = optimal_path['optimal_path']

    st.markdown(f"Response from API = {path}")