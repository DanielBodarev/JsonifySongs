from SongStructure.TextBlock import TextBlock
from Common import Settings
from SongAnalyzer.SongProperties import Part

verse_regex = Settings.song.get("verseregex")
class Verse(TextBlock):
    def __init__(self, text):
        self.part = Part.Verse
        super().__init__(text, verse_regex, "1.")
