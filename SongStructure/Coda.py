from SongStructure.TextBlock import TextBlock
from Common import Settings
from SongAnalyzer.SongProperties import Part

coda_regex = Settings.song.get("codaregex")
class Coda(TextBlock):
    def __init__(self, text):
        self.part = Part.Coda
        super().__init__(text, coda_regex, "C:")
