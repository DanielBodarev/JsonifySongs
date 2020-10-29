from SongStructure.TextBlock import TextBlock
from Common import Settings

refrain_regex = Settings.song.get("refrainregex")
class Refrain(TextBlock):
    def __init__(self, text):
        super().__init__(text, refrain_regex, "R:")
