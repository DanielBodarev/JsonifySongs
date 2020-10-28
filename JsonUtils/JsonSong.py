class JsonSong:
    
    def __init__(self, textblocks, title):
        self.textblocks = self._textblock_as_json_format(textblocks)
        self.title = title

    def get_as_json_format(self):
        result = {
            "Verses" : self.textblocks,
            "Text" : self.title
        }

        return result

    def _textblock_as_json_format(self, textblock):
        result = [
            {"Text" : str(text)} for text in textblock
        ]

        return result

