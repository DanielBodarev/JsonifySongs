from SongLogic.ISongLogic import ISongLogic
from Common import StringUtils as SU

class Traditional(ISongLogic):

    def __init__(self, song):
        self.song = song

    def get_title(self):
        first_verse = self.song.verses[0].text
        title = SU.get_first_words_with_limits(first_verse)
        return title

    def get_sequenced_song(self):
        result = []
        verses = self.song.verses
        refrain = self.song.refrains[0]

        for index, verse in enumerate(verses):
            result.append(verse)
            if index < len(verses):
                result.append(refrain)

        return result