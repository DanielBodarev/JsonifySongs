from SongLogic.ISongLogic import ISongLogic
from Common import StringUtils as SU

class Rondo(ISongLogic):

    def __init__(self, song):
        self.song = song

    def get_title(self):
        first_verse = self.song.verses[0].text
        title = SU.get_first_words_with_limits(first_verse)
        return title

    def get_sequenced_song(self):
        result = []
        if (len(self.song.refrains) == len(self.song.verses)):
            result = self._get_evenly_interlaced()
        else:
            result = self._get_unevenly_interlaced()
        return result

    def _get_evenly_interlaced(self):
        result = []
        for index, verse in enumerate(self.song.verses):
            result.append(verse)
            result.append(self.song.refrains[index])
        return result

    def _get_unevenly_interlaced(self):
        result = []
        verses = self.song.verses
        refrains = self.song.refrains
        while verses or refrains:
            if verses:
                result.append(verses[0])
                verses = verses[1:]
            if refrains:
                result.append(refrains[0])
                refrains = refrains[1:]
        return result