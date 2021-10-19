"""Spotify API"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

with open('key.txt', 'r') as file:
    client_ID = file.readline()
    client_secret = file.readline()

credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials_manager)
