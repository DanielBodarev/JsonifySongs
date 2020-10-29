from Common import Settings
from SongAnalyzer.SongProperties import Part

from SongStructure.TextBlock import TextBlock

refrain_regex = Settings.song.get("refrainregex")
class Refrain(TextBlock):
    def __init__(self, text):
        self.part = Part.Refrain
        super().__init__(text, refrain_regex, "R:")
