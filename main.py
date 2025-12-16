# Most streamed spotify songs 2023
import pandas as pd
df = pd.read_csv("/workspaces/Coding2-PANDAS-Project/spotify-2023-clean.csv")

#Create class for the spotify data set
class data_set: 
    # Initialize data set
    def __init__(self, set): 
        self.data_set = set

    # Remove unecessary columns from the data set
    def clean_data(self): 
        self.data_set.pop("in_apple_playlists")
        self.data_set.pop("in_apple_charts")
        self.data_set.pop("in_deezer_playlists")
        self.data_set.pop("in_deezer_charts")
        self.data_set.pop("in_shazam_charts")
        self.data_set.pop("key")
        self.data_set.pop("mode")
    
    # Have user input an artist and song value (ex.danceabiltiy) and recommennd song by artist with the highest score for that value
    def recommend_song(self, artist, value): # by danceabiltiy etc. 
        artist_sorted = self.data_set.loc[self.data_set["artist(s)_name"] == artist]
        recommended = artist_sorted.sort_values(by = value, ascending = False)
        return recommended.head(1)     

    # Return artist's most popular song
    def most_popular_song(self, artist, value): # artist most popular song in 2023 
    # In UI, pass streams to value when calling this function
        artist_sorted = self.data_set.loc[self.data_set["artist(s)_name"] == artist]
        most_popular = artist_sorted.sort_values(by = value, ascending = False)

    # Create a mini playlist for the user based on the values of a song that the user inputted
    def mini_playlist(self, song): 
        index = int((df.loc[df['track_name'] == song]).index[0])
        acousticness = df.loc[index]["acousticness_%"]
        danceability =  df.loc[index]["danceability_%"]
        energy = df.loc[index]["energy_%"]
        valence = df.loc[index]["valence_%"]
        instrumentalness = df.loc[index]["instrumentalness_%"]
        bpm = df.loc[index]["bpm"]
        playlist = []
        #acousticness
        track_1 = int((df.loc[df['acousticness_%'] == (acousticness - 1)]).index[0])
        name_1 = df.loc[track_1]["track_name"]
        playlist.append(name_1)
        #danceability
        track_2 = int((df.loc[df['danceability_%'] == (danceability - 1)]).index[0])
        name_2 = df.loc[track_2]["track_name"]
        playlist.append(name_2)
        #energy
        track_3 = int((df.loc[df['energy_%'] == (energy - 1)]).index[0])
        name_3 = df.loc[track_3]["track_name"]
        playlist.append(name_3)
        #valence
        track_4 = int((df.loc[df['valence_%'] == (valence - 1)]).index[0])
        name_4 = df.loc[track_4]["track_name"]
        playlist.append(name_4)
        #instrumentalness
        track_5 = int((df.loc[df['instrumentalness_%'] == (instrumentalness - 1)]).index[0])
        name_5 = df.loc[track_5]["track_name"]
        playlist.append(name_5)
        #bpm
        track_6 = int((df.loc[df['bpm'] == (bpm - 1)]).index[0])
        name_6 = df.loc[track_6]["track_name"]
        playlist.append(name_6)
    
        return playlist
        
        ## TO DO: 
        # Sam: Create UI

harshita = data_set(df)
harshita.clean_data()
# harshita.recommend_song("Taylor Swift", "acousticness_%")
print(harshita.mini_playlist("Columbia"))
#index = int((df.loc[df['track_name'] == "Columbia"]).index[0])
#print(index)

