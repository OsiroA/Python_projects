from flask import Flask, request, redirect, render_template
import requests
import os
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        year = request.form['year']
        songs = searchByYear(year)
        return render_template('result.html', songs=songs)

def searchByYear(year):
    clientID = os.environ['CLIENT_ID']
    clientSecret = os.environ['CLIENT_SECRET']

    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSecret)

    response = requests.post(url, data=data, auth=auth)

    accessToken = response.json()["access_token"]

    url = "https://api.spotify.com/v1/search"
    headers = {'Authorization': f'Bearer {accessToken}'}

    search = f"?q=year%3A{year}&type=track&limit=10"

    fullURL = f"{url}{search}"

    response = requests.get(fullURL, headers=headers)

    data = response.json()

    trackInfo = []
    for track in data["tracks"]["items"]:
        for artist in track["artists"]:
            trackInfo.append({
                "Artist Name": artist["name"],
                "Track Name": track["name"],
                "Preview URL": track["preview_url"]
            })

    return trackInfo

app.run(host='0.0.0.0', port=81)
