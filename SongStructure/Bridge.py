from SongStructure.TextBlock import TextBlock
from Common import Settings

bridge_regex = Settings.song.get("bridgeregex")
class Bridge(TextBlock):
    def __init__(self, text):
        super().__init__(text, bridge_regex, "B: ")
