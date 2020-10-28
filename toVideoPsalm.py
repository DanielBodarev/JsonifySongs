from SongStructure.Verse import Verse
from SongStructure.Refrain import Refrain
from SongStructure.Song import Song
from JsonUtils.JsonConverter import save_songs

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

save_songs(song)
