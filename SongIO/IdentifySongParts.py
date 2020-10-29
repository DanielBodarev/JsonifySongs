import re

from Common import Settings
from SongStructure.Bridge import Bridge
from SongStructure.Coda import Coda
from SongStructure.Refrain import Refrain
from SongStructure.Verse import Verse

regi = {
    Settings.song.get("bridgeregex") : Bridge,
    Settings.song.get("codaregex") : Coda,
    Settings.song.get("refrainregex") : Refrain
}

def get_song_part(text):
    for regex in regi:
        match = re.search(regex, text)
        if match:
            return regi[regex]
    return Verse