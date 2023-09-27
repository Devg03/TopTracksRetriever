import requests
from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = ' '
SPOTIFY_ACCESS_TOKEN = ' '


def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

def main():
    current_track_info = get_current_track(
        SPOTIFY_ACCESS_TOKEN
    )

    pprint(current_track_info, indent = 4)

if __name__ == '__main__':
    main() 