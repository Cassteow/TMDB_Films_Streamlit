import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests

def getToken():
    token = {
        "accept": "application/json",
        "Authorization": st.secrets["Authorization"],
    }
    return token

class APIConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs) -> requests.Session:
        session = requests.Session()
        session.headers['Authorization'] = 'Bearer ' + kwargs['token']
        return session
    
    def get_popular_movies(self):
        url = "https://api.themoviedb.org/3/movie/popular"

        # call API
        response = self._instance.get(url, headers=self._connect().token)
        # check response status code
        if response.status_code != 200:
            st.error("Error retrieving data from TMDB API")
        else:
            return response.json()['results']            
