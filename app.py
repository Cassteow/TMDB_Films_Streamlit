import streamlit as st
import pandas as pd
from streamlit.connections import ExperimentalBaseConnection
from api_connection import APIConnection
from api_connection import getToken


# Set page config
st.set_page_config(page_title="TMDB Top Movies", layout="wide", page_icon="🎬")
# Set page title
st.title("TMDB Top Movies")

# Get token
token = getToken()
# Connect to TMDB API
conn = st.experimental_connection("tmdb_api", type=APIConnection, token=getToken())

# create dataframe from API response
columns = ["title", "release_date", "vote_average", "overview"]
data = pd.DataFrame(columns=columns)
# write response 
st.write("Top 10 movies:")
st.write(conn.get_popular_movies()[:10])

# Display dataframe
st.session_state.data = data
st.write(data)