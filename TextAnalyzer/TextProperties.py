from enum import Enum

class Amount(Enum):
    None = auto(),
    One = auto(),
    Many = auto()

class Part(Enum):
    Verse = auto(),
    Refren = auto(),
    Coda = auto(),
    Bridge = auto()
