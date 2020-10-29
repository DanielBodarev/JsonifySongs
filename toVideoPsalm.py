from Common import Settings
from JsonUtils.JsonSongbook import JsonSongbook
from SongIO import FromFolder, SaveSongbook

source_folder = Settings.misc.get("sourcefolder")

song_arrays = get_song_array_from_folder(source_folder)
songbook = JsonSongbook(song_arrays)
save_songbook(songbook)