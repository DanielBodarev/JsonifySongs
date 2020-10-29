from SongIO import FromFolder
from SongIO import SaveSongbook
from JsonUtils.JsonSongbook import JsonSongbook

song_arrays = get_song_array_from_folder("path")
songbook = JsonSongbook(song_arrays)
save_songbook(songbook)
