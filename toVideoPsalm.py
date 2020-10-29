from JsonUtils.JsonConverter import songbook_to_json_format
from JsonUtils.JsonSongbook import JsonSongbook
from SongStructure.Refrain import Refrain
from SongStructure.Song import Song
from SongStructure.Verse import Verse
from Common import Settings
import os
import re

verses = [
    Verse("1. This is verse one. It's a very good song"),
    Verse("2. This is verse two. Hope you enjoy it too"),
    Verse("3. This is verse three. It's all we can sing"),
]

refrains = [
    Refrain("Refren: We now have the refrain. Sing the refrain")
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