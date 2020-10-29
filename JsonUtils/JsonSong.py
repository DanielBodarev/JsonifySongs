from Common import Settings

footer = Settings.song.get("footer")
class JsonSong:
    
    def __init__(self, textblocks, title):
        self.textblocks = self._textblock_as_json_format(textblocks)
        self.title = title

    def get_as_json_format(self):
        self._append_footer()
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

    def _append_footer(self):
        if footer and self.textblocks:
            self.textblocks[-1]["Text"] = self.textblocks[-1]["Text"] + "\n" + footer

