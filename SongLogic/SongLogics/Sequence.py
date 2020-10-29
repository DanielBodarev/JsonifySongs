from SongLogic.ISongLogic import ISongLogic
from Common import StringUtils as SU

class Sequence(ISongLogic):

    def __init__(self, song):
        self.song = song

    def get_title(self):
        first_verse = self.song.verses[0].text
        title = SU.get_first_words_with_limits(first_verse)
        return title

    def get_sequenced_song(self):
        return self.song.verses