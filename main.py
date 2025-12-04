# Most streamed spotify songs 2023
import pandas as pd
df = pd.read_csv("/workspaces/Coding2-PANDAS-Project/spotify-2023-clean.csv")

# df.head()
# df.describe()
# df.columns()

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
    
    # def recommend_song(self, artisit, value): 
        #Have code give song that meets cirteria and is most populaarrrr
    # def most_popular_song(self, artist): lkk
        #Gives most popular song by artist

    #Also make a who sings this? function

