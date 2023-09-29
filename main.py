from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get


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
    json_result = json.loads(result.content)
    print(json_result) # Prints to ensure the functionality


token = get_token()
search_for_artist(token, "ACDC") # Searchig for ACDC
