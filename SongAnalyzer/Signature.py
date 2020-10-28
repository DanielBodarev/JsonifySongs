
class Signature:
    def __init__(self, bridges, codas, refrains, verses):
        self.bridges = bridges
        self.codas = codas
        self.refrains = refrains
        self.verses = verses

    def __eq__(self, other):
        return self.bridges == other.bridges and self.codas == other.codas and self.refrains == other.refrains and self.verses == other.verses
