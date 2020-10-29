import json
import re

from Common import Settings
from SongLogic import SongLogicFactory

from JsonUtils.JsonSong import JsonSong
from JsonUtils.JsonSongbook import JsonSongbook

def song_to_json_song(song):
    song_logic = SongLogicFactory.get_song_logic(song)
    textblocks = song_logic.get_sequenced_song()
    title = song_logic.get_title()
    json_song = JsonSong(textblocks, title).get_as_json_format()
    return json_song

def songbook_to_json_format(songbook):
    js_songbook = songbook.get_as_json_format()
    json_string = json_dumps_videopsalm_format(js_songbook, {'indent' : Settings.misc.getint("json_indent")})
    return json_string

def json_dumps_videopsalm_format(text, kwargs):
    result = json.dumps(text, **kwargs)
    result = _remove_quotes_from_keys(result)
    result = _remove_escape_from_newline(result)
    return result

def _remove_quotes_from_keys(json_text):
    return re.sub(r'"(.*?)"[ ]*?:', r'\1:', json_text)

def _remove_escape_from_newline(json_text):
    return json_text.replace(r"\n", "\n")