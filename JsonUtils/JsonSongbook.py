class JsonSongbook:

    def __init__(self, songbook_name, json_songs):
        self.songbook_name = songbook_name
        self.json_songs = json_songs
        self.guid = "60g30Z4xsESNEmW8Las0eg"

    def get_as_json_format(self):
        result = {
            "Songs" : self.json_songs,
            "Guid" : self.guid,
            "Text": self.songbook_name
        }

        return result