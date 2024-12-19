import streamlit as st
import json
import requests

st.title("Travel Agent: Finding the optimal path")

departure_city = st.selectbox('Departing City',
                              ("San Diego, CA", "St. Johns, NL", "Washington, DC"))