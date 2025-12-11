# Most streamed spotify songs 2023
import pandas as pd
df = pd.read_csv("/workspaces/Coding2-PANDAS-Project/spotify-2023-clean.csv")

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
    
    def recommend_song(self, artist, value): # by danceabiltiy etc. 
        artist_sorted = self.data_set.loc[self.data_set["artist(s)_name"] == artist]
        recommended = artist_sorted.sort_values(by = value, ascending = False)
        return recommended.head(1)     

    def most_popular_song(self, artist, value): # artist most popular song in 2023 
    # In UI, pass streams to value when calling this function
        artist_sorted = self.data_set.loc[self.data_set["artist(s)_name"] == artist]
        most_popular = artist_sorted.sort_values(by = value, ascending = False)

    # def mini_playlist(self, song): 
    # # make playlist based off song given by user and finding songs with similar descriptive values; like 5 songs


harshita = data_set(df)
harshita.clean_data()
harshita.recommend_song("Taylor Swift", "acousticness_%")
