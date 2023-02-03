import requests
import config
import csv
from datetime import date

auth_url = 'https://accounts.spotify.com/api/token'  # authorization url
base_url = 'https://api.spotify.com/v1/'  # base URL of all Spotify API endpoints
playlist = "BILLIONS CLUB"  # tracked playlist
playlist_id = "37i9dQZF1DX7iB3RCnBnN4"  # spotify's id for playlist

if __name__ == '__main__':

    # post authorization
    auth = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': config.client_id,
        'client_secret': config.client_secret,
    })

    # access token
    token = auth.json()['access_token']

    # headers
    headers = {'Authorization': 'Bearer {token}'.format(token=token)}

    # get request for playlist
    r = requests.get(base_url + 'playlists/' + playlist_id, headers=headers)

    # number of followers in the playlist
    num_followers = r.json()["followers"]['total']

    # get date
    today = date.today()

    # open file
    with open('followers.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # append data
        writer.writerow([today, num_followers])
