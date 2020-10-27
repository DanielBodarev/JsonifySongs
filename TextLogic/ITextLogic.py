from abc import ABC, abstractmethod

class ITextLogic(ABC):

    def __init__(self, song):
        self.song = song
    
    @abstractmethod
    def get_sequenced_song(self):
        pass
