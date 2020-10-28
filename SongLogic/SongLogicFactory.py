from SongAnalyzer.SongPropertyChecker import SongPropertyChecker
from SongAnalyzer.SongProperties import Amount, Part
from SongLogic.SongLogics.Traditional import Traditional
from SongAnalyzer.Signature import Signature

_signatures = [
    [Signature(bridges=Amount.Zero, codas=Amount.Zero, refrains=Amount.One, verses=Amount.Many),
    Traditional]
]

def get_song_logic(song):
    checker = SongPropertyChecker(song)
    props = checker.get_song_properties()
    logic = _get_matching_signature(props)
    return logic(song)

def _get_matching_signature(properties):
    for signature in _signatures:
        if signature[0] == properties:
            return signature[1]
