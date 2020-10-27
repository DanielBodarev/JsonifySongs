import TextAnalyzer.TextProperties as Props

class TextPropertyChecker:

    def __init__(self, song):
        self.song = song

    def get_text_properties(self):
        properties = {}
        for prop in Props:
            properties[prop] = self.get_property(prop)
        return properties

    def get_property(self, part):
        if self._has_none(part):
            return Amount.None
        if self._has_one(part):
            return Amount.One
        if self._has_one(part):
            return Amount.Many

    def _has_none(self, part):
        return len(self.song.get_part(part)) <= 0

    def _has_one(self, part):
        return len(self.song.get_part(part)) == 1

    def _has_many(self, part):
        return len(self.song.get_part(part)) > 1
