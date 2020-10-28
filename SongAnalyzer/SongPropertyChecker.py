from SongAnalyzer.SongProperties import Amount, Part
from SongAnalyzer.Signature import Signature

class SongPropertyChecker:

    def __init__(self, song):
        self.song = song

    def get_song_properties(self):
        _bridges = self.get_property(Part.Bridge)
        _codas = self.get_property(Part.Coda)
        _refrains = self.get_property(Part.Refrain)
        _verses = self.get_property(Part.Verse)
        return Signature(bridges=_bridges, codas=_codas, refrains=_refrains, verses=_verses)

    def get_property(self, part):
        if self._has_none(part):
            return Amount.Zero
        if self._has_one(part):
            return Amount.One
        if self._has_many(part):
            return Amount.Many

    def _has_none(self, part):
        return len(self.song.get_part(part)) <= 0

    def _has_one(self, part):
        return len(self.song.get_part(part)) == 1

    def _has_many(self, part):
        return len(self.song.get_part(part)) > 1
