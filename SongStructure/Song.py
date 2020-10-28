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
        self.title = "-"

    def get_part(self, part):
        return self.map[part]

    def add_verse(self, verse):
        self.verses.append(verse)

    def add_verses(self, verses):
        for verse in verses:
            self.add_verse(verse)

    def add_refrain(self, refrain):
        self.refrains.append(refrain)

    def add_refrains(self, refrains):
        for refrain in refrains:
            self.add_refrain(refrain)

    def add_coda(self, coda):
        self.codas.add(coda)

    def add_codas(self, codas):
        for coda in codas:
            self.add_coda(verse)

    def add_bridge(self, bridge):
        self.bridges.add(bridge)

    def add_bridges(self, bridges):
        for bridge in bridges:
            self.add_bridge(bridge)
