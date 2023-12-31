import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests

@st.cache_data
def getToken():
    token = st.secrets["token"]
    return token


class APIConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs) -> requests.Session:
        session = requests.Session()
        session.headers['accept'] = 'application/json'
        session.headers['Authorization'] = 'Bearer ' + kwargs['token']
        return session
    
    def cursor(self):
        return self._resource
    
    def get_popular_movies(self):
        url = "https://api.themoviedb.org/3/movie/popular?page=1"
        # call API
        response = self._instance.get(url)
        # check response status code
        if response.status_code != 200:
            return None
        else:
            return response.text   
        
    def get_top_rated_movies(self):
        url = "https://api.themoviedb.org/3/movie/top_rated?page=1"
        # call API
        response = self._instance.get(url)
        # check response status code
        if response.status_code != 200:
            return None
        else:
            return response.text
