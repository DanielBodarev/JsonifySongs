from SongStructure.TextBlock import TextBlocks
from Common import Settings

coda_regex = Settings.song.get("codaregex")
class Coda(TextBlock):
    def __init__(self, text):
        super().__init__(text, coda_regex, "C:")
