# Most streamed spotify songs 2023
import pandas as pd
df = pd.read_csv("/workspaces/Coding2-PANDAS-Project/spotify-2023.csv")

class data_set: 
    def __init__(self, set): 
        self.data_set = set

    def clean_data(self): 
        self.data_set.pop("in_apple_playlists")
        self.data_set.pop("in_apple_charts")
        self.data_set.pop("in_deezer_playlists")
        self.data_set.pop("in_deezer_charts")
        self.data_set.pop("in_shazam_charts")
        self.data_set.pop("key")
        self.data_set.pop("mode")
    
    def recommend_song(self, artisit, value): # by danceabiltiy etc. 
        recommended = df.sort_values(by = '')

    def most_popular_song(self, artist): # artist most popular song in 2023

    def mini_playlist(self, song): 
    # make playlist based off song given by user and finding songs with similar descriptive values; like 5 songs

