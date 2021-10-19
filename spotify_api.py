"""Spotify API"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_ID = 'e385f499ac7d4707b9fe728b87e0b082'
client_secret = '4957616893f4447d9dade1bb492c62f7'
credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials_manager)
