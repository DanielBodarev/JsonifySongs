import TextAnalyzer.TextProperties as Props

class Song:
    def __init__(self):
        self.verses = []
        self.refren = []
        self.codas = []
        self.bridges = []
        self.map = {
            Part.Verse : self.verses,
            Part.Refren: self.refren,
            Part.Coda : self.codas,
            Part.Bridge : self.bridges
        }

    def get_part(self, part):
        return self.map[part]

    def add_verse(self, verse):
        self.verses.append(verse)

    def add_refren(self, refren);
        self.refren.append(refren)

    def add_coda(self, coda):
        self.codas.add(coda)

    def add_bridge(self, bridge):
        self.bridges.add(bridge)
