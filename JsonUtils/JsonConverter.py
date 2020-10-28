import json
from JsonUtils.JsonSong import JsonSong
from JsonUtils.JsonSongbook import JsonSongbook
from SongLogic import SongLogicFactory

def song_to_json_format(song):
    song_logic = SongLogicFactory.get_song_logic(song)

    textblocks = song_logic.get_sequenced_song()
    title = song_logic.get_title()

    json_song = JsonSong(textblocks, title)

    json_formatted_song = json_song.get_as_json_format()

    return json_formatted_song

path = "C:/Users/Public/Documents/VideoPsalm/SongBooks/test.json"
def save_songs(song):
    js_song = song_to_json_format(song)
    js_songbook = JsonSongbook("testhopeitworks", [js_song]).get_as_json_format()
    with open(path, 'w') as outfile:
        json_string = json.dumps(js_songbook, indent=1)
        json_string = json_string.replace('"Songs"', 'Songs')
        json_string = json_string.replace('"Guid"', 'Guid')
        json_string = json_string.replace('"Verses"', 'Verses')
        json_string = json_string.replace('"Text"', 'Text')
        json_string = json_string.replace('"VideoDuration"', 'VideoDuration')
        outfile.write(json_string)

