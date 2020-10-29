from Common import Settings
from JsonUtils.JsonSong import JsonSong
from JsonUtils import JsonConverter

default_name = Settings.songbook.get("filename") 
default_path = Settings.songbook.get("path")
class JsonSongbook:

    def __init__(self, json_songs=[], songbook_name=default_name):
        self.songbook_name = songbook_name
        self.json_songs = json_songs

    def add_song(self, song):
        self.json_songs.append(JsonConverter.song_to_json_song(song))

    def get_as_json_format(self):
        result = {
            "Songs" : self.json_songs,
            "Style" : {"Body" : {
                "VerticalAlignment" : Settings.songbook.getint("verticalalignment"),
                "Transition" : Settings.songbook.getint("transition"),
            }},
            "Text" : self.songbook_name
        }

        return result

    def get_json_path(self):
        return default_path + default_name + ".json"