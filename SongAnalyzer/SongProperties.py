from enum import Enum, auto

class Amount(Enum):
    Zero = 1,
    One = 2,
    Many = 3

class Part(Enum):
    Verse = auto(),
    Refrain = auto(),
    Coda = auto(),
    Bridge = auto()
