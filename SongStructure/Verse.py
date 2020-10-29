from SongStructure.TextBlock import TextBlock
from Common import Settings

verse_regex = Settings.song.get("verseregex")
class Verse(TextBlock):
    def __init__(self, text):
        super().__init__(text, verse_regex, "1.")
