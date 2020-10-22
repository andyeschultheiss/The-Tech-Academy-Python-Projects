"""
Step #1: Log into YouTube
Step #2: Get Liked Videos
Step #3: Create New Playlist
Step #4: Search for the Song
Step #5: Add Song to new Spotify Playlist

"""

import json
import requests
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtube_dl

class CreatePlaylist:

    def __init__(self):
        self.user_id = "f77edfcb337d42f8b812d3ec3d626569"
        self.spotify_token =  "b0ba307593f542d5af51c1afcb55534d"
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}

    ## Step #1: Log into YouTube
    def get_youtube_client(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # get credentials and create API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_console()

        # from YouTube DATA API
        youtube_client = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

        return youtube_client      

    ## Step #2: Get Liked Videos
    def get_liked_videos(self):
        request = self.youtube_client.videos().list(
            part = "snippet,contentDetails,statistics",
            myRating = "like"
        )
        response = request.execute()

        # collect each video and get info
        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = "https://www.youtube.com/watch?v={}".format(item["id"])

            # use youtube_dl to collect song name & artist name
            video = youtube_dl.YoutubeDL({}).extract_info(youtube_url, download=False)
            song_name = video["track"]
            artist = video["artist"]

            # save important info
            self.all_song_info[video_title] = {
                "youtube_url": youtube_url,
                "song_name": song_name,
                "artist": artist,
                # add uri
                "spotify_uri": self.get_spotify_uri(song_name, artist)
            }
        
    ## Step #3: Create New Playlist
    def create_playlist(self):
        
        request_body = json.dumps({
            "name": "YouTube Liked Videos",
            "description": "All liked YouTube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data = request_body,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )

        response_json = response.json()

        # return playlist id
        return response_json["id"]

    ## Step #4: Search for the Song
    def get_spotify_uri(self, song_name, artist):

        request_body = json.dumps({
            "name": "YouTube Liked Videos",
            "description": "All liked YouTube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/search?q=track%3A{}+artist%3A{}&type=track&limit=10".format(
            song_name,artist
        )

        response = requests.get(
            query,
            data = request_body,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )

        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # just first song
        uri = songs[0]["uri"]

        return uri

    ## Step #5: Add Song to new Spotify Playlist
    def add_song_to_playlist(self):
        # populate song dictionary
        self.get_liked_videos()

        # collect all uris  
        uris = []
        for song, info in self.all_song_info.items():
            uri.append(info["spotify_uri"])

        # create new playlist
        playlist_id = self.create_playlist()

        # add all songs to playlist
        request_data = json.dumps(uris)
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
        response = requests.post(
            query,
            data=request_data,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )
        response_json = response.json()
        return response_json



