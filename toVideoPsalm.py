from Common import Settings
from JsonUtils.JsonSongbook import JsonSongbook
from SongIO import FromFolder, SaveSongbook

source_folder = Settings.misc.get("sourcefolder")

song_arrays = FromFolder.get_song_array_from_folder(source_folder)
songbook = JsonSongbook(song_arrays)
SaveSongbook.save_songbook(songbook)