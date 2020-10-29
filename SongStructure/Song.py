from SongAnalyzer.SongProperties import Part, Amount

class Song:
    def __init__(self):
        self.verses = []
        self.refrains = []
        self.codas = []
        self.bridges = []
        self.map = {
            Part.Verse : self.verses,
            Part.Refrain: self.refrains,
            Part.Coda : self.codas,
            Part.Bridge : self.bridges
        }

    def get_part(self, part):
        return self.map[part]

    def add_song_part(self, song_part):
        self.get_part(song_part.part).append(song_part)