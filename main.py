import base64
import json
import os

from dotenv import load_dotenv
from requests import get, post

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")

# print(client_id, client_secret_id)

def get_token():
    auth_string = client_id + ":" + client_secret_id
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = { "Authorization": "Basic " + auth_base64, "Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_headers(token):
    return {"Authorization": "Bearer " + token}

# Function to search for artists
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search" #What spotify url to request from
    headers = get_auth_headers(token)
    query = f"?q={artist_name}&type=artist&limit = 1" # Defines query. q = searching for what, & lets you type the type of content you are querying and limit sets the number of results

    query_url = url + query
    result = get(query_url, headers = headers) # Stores the returned headers
    json_result = json.loads(result.content)["artists"]["items"] # Only searches for the artists name and related info.

    # If no artists exists by that name then returns the following
    if len(json_result) == 0:
        print("No artist with the name entered exists....")
        return None
    
    return json_result[0] # If the artists exists then the returns the info.


# Function to search for top-tracks based on the artist_id which is a must for SpotifyAPI to search anything related to an artist
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

token = get_token()
result = search_for_artist(token, "ACDC") # Searchig for ACDC
artist_id = result["id"] #stores the id of the artists
songs = get_songs_by_artist(token, artist_id) #stores the results of the query for top tracks


# Returns the list of top tracks and numbers them
for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")
