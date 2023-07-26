import streamlit as st
import pandas as pd
from streamlit.connections import ExperimentalBaseConnection
from api_connection import APIConnection
from api_connection import getToken


# Set page config
st.set_page_config(page_title="TMDB Top Movies", layout="wide", page_icon="🎬")
# Set page title
st.title("TMDB Top Movies")

# Connect to TMDB API
conn = st.experimental_connection("tmdb_api", type=APIConnection)

# create dataframe from API response
columns = ["title", "release_date", "vote_average", "overview"]
data = pd.DataFrame(columns=columns)
for movie in conn.get_popular_movies():
    title = movie['title']
    release_date = movie['release_date']
    vote_average = movie['vote_average']
    overview = movie['overview']
    data = data.append(
        pd.Series([title, release_date, vote_average, overview], index=columns),
        ignore_index=True,
    )

# Display dataframe
st.session_state.data = data
st.write(data)