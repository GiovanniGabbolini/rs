import pandas as pd
import matplotlib.pyplot as plt
import data

playlists = data.get_playlists_df()
tracks = data.get_tracks_df()

join = playlists.merge(tracks, on='track_id')

only_albums = join[['playlist_id','album_id']]
print(only_albums)

only_albums.plot(x='playlist_id', y='album_id')

plt.show(block=True)
print(0)