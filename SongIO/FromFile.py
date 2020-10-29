from SongStructure.Song import Song
from SongIO import FileReader
from SongIO import IdentifySongParts

def create_song_from_file(filename):
    song = Song()
    text_array = read_as_string_array(filename)
    for text in text_array:
        song_part = get_song_part(text)
        part = song_part(text)
        song.add_song_part(part)
    return song