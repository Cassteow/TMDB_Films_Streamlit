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
# write response 
st.write("Top 10 movies:")

response = conn.get_popular_movies()
st.write(response)

movies_data = response["results"]
movie_info = []

for movie in movies_data:
    title = movie["title"]
    release_date = movie["release_date"]
    vote_average = movie["vote_average"]
    overview = movie["overview"]
    movie_info.append([title, release_date, vote_average, overview])
    
columns = ["Title", "Vote Average", "Release Date", "Overview"]
movies_df = pd.DataFrame(movie_info, columns=columns)
# Display movies_df
st.write(movies_df)

