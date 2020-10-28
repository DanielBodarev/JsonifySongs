class JsonSong:
    
    def __init__(self, textblocks, title):
        self.textblocks = self._textblock_as_json_format(textblocks)
        self.title = title
        self.guid = "60g30Z4xsESNEmW8Las0eg"
        self.video_duration = 0

    def get_as_json_format(self):
        result = {
            "Guid" : self.guid,
            "Verses" : self.textblocks,
            "VideoDuration" : self.video_duration,
            "Text" : self.title
        }

        return result

    def _textblock_as_json_format(self, textblock):
        result = [
            {"Text" : str(text)} for text in textblock
        ]

        return result

