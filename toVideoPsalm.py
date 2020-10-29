from JsonUtils.JsonConverter import songbook_to_json_format
from JsonUtils.JsonSongbook import JsonSongbook
from SongStructure.Refrain import Refrain
from SongStructure.Song import Song
from SongStructure.Verse import Verse
from Common import Settings
import os

verses = [
    Verse("This is verse one. It's a very good song"),
    Verse("This is verse two. Hope you enjoy it too"),
    Verse("This is verse three. It's all we can sing"),
]

refrains = [
    Refrain("We now have the refrain. Sing the refrain")
]

song = Song()
song.add_verses(verses)
song.add_refrains(refrains)

sb = JsonSongbook()
sb.add_song(song)

path = sb.get_json_path()

json_string = songbook_to_json_format(sb)

with open(path, 'w') as outfile:
    print(json_string)
    outfile.write(json_string)
