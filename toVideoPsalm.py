import json
from SongStructure.Verse import Verse
from SongStructure.Refrain import Refrain
from SongStructure.Song import Song
from SongLogic import SongLogicFactory
"""
with open('Speranta.json') as json_file:
    data = json.load(json_file)"""

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

song_logic = SongLogicFactory.get_song_logic(song)

print([str(x) for x in song_logic.get_sequenced_song()])
