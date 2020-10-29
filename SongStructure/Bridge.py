from SongStructure.TextBlock import TextBlock
from Common import Settings
from SongAnalyzer.SongProperties import Part

bridge_regex = Settings.song.get("bridgeregex")
class Bridge(TextBlock):
    def __init__(self, text):
        self.part = Part.Bridge
        super().__init__(text, bridge_regex, "B: ")
