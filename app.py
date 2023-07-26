import streamlit as st
import pandas as pd
from streamlit.connections import ExperimentalBaseConnection
from api_connection import APIConnection
from api_connection import getToken
import json


# Set page config
st.set_page_config(page_title="TMDB Top Movies", layout="wide", page_icon="🎬")
# Set page title
st.title("TMDB Top Movies")
# Get token
token = getToken()
# Connect to TMDB API
conn = st.experimental_connection("tmdb_api", type=APIConnection, token=getToken())

# set dropdown menu to select movie type
movie_type = st.selectbox("Select movie type", ("Popular", "Top Rated"))
row_button = st.columns((3,2,2,3)) 
# submit and reset button in green colour
submit = row_button[1].button('Submit') 
reset = row_button[2].button('Reset')
result = False

if submit:
    result = True

if reset:
    result = False

if result:
    if movie_type == "Popular":
        response = conn.get_popular_movies()
    else:
        response = conn.get_top_rated_movies()


    # create dataframe from API response
    columns = ["title", "release_date", "vote_average", "overview"]
    # write response 
    st.write("Top 20 movies:")

    response = conn.get_popular_movies()
    # print response data type
    #st.write(response)

    if response != None:
        #movies_data = json.loads(response.text)
        movie_info = []

        for movie in response:       
            title = movie['title']
            release_date = movie['release_date']
            vote_average = movie['vote_average']
            overview = movie['overview']
            movie_info.append([title, release_date, vote_average, overview])
            
        columns = ["Title",  "Release Date","Vote Average", "Overview"]
        movies_df = pd.DataFrame(movie_info, columns=columns)
        # Display movies_df
        st.write(movies_df)

    else:
        st.write("Error: API call failed")