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
        return most_popular.head(1)

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
        #track_5 = int((df.loc[df['instrumentalness_%'] == (instrumentalness - 1)]).index[0])
        #name_5 = df.loc[track_5]["track_name"]
        #playlist.append(name_5)
        #bpm
        track_6 = int((df.loc[df['bpm'] == (bpm - 1)]).index[0])
        name_6 = df.loc[track_6]["track_name"]
        playlist.append(name_6)
    
        return playlist
        
# UI:
# Making the main dataset and cleaning dataset
songs = data_set(df)
songs.clean_data()

# Main UI Loop:
while 0 == 0:
    #This part prompts the user for which of 3 methods included in the data_set class they want to use
    # UI Bar is printed in the UI for formatting. It makes it look much cleaner, rather than a wall of text.
    ui_bar = "__________________________________________________________________________________"
    print(ui_bar)
    print("Press 1 to get recommended a song.")
    print("Press 2 to get an artists most popular song.")
    print("Press 3 to get recommended a playlist.")
    option = int(input("Option: "))
    print(ui_bar)
    if option == 1:
        # Here, we use the reccomend song method, and prompt the user for an artist choice, and then their favorite song quality listed.
        artist = input("What artist do you like: ")
        print("Choose a song element that is most important to you. Choices are:")
        print("1: Danceability")
        print("2: Valence")
        print("3: Energy")
        print("4: Acousticness")
        print("5: Instrumentalness")
        print("6: Liveness")
        print("7: Speechiness")
        print(ui_bar)
        v = " "
        # These if statements are needed because the value keys need to match exactly as the csv file has them. 
        value = int(input("Choose the number option most important to you: "))
        if value == 1:
            v = "danceability_%"
        elif value == 2:
            v = "valence_%"
        elif value == 3:
            v = "energy_%"
        elif value == 4:
            v = "acousticness_%"
        elif value == 5:
            v = "instrumentalness_%"
        elif value == 6:
            v = "liveness_%"
        elif value == 7:
            v = "speechiness_%"
        else:
            print("An incorrect value was entered!")
            v = 0
        if v != 0:
            print(ui_bar)
            print("Song: ")
            # This prints the closest song to the options entered above.
            print(songs.recommend_song(artist, v)["track_name"])
    elif option == 2:
        # This uses the method in our class to find the most streamed song by a certain artist. It asks for the artist name.
        artist = input("Enter Artist Name: ")
        print(ui_bar)
        print("Song: ")
        # This runs the method, with the artist entered. It uses "streams" as a value, and is indexed by track_name for cleaner output.
        print(songs.most_popular_song(artist, "streams")["track_name"])
    elif option == 3:
        # This method makes a playlist for a user based on qualities of an entered song.
        print("This will construct a playlist of similar songs to the song entered.")
        # Here, we ask for the song.
        track = input("Enter the song you want the playlist to be based off of: ")
        print(ui_bar)
        print("Playlist: ")
        # This for loop provides cleaner output. It prints the songs in the returned list line by line. The "mini_playlist" is our actual call.
        for i in songs.mini_playlist(track):
            print(i)
