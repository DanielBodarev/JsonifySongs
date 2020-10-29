import re

# Wait until I know the format

def read_as_string_array(filepath):
    song_string = _read_file(filepath)
    string_array = _split_song_string(song_string)

def _read_file(filepath):
    extension = filepath.split(".")[-1]
    
def _read_txt_file(filepath):
    with open(filepath) as file:
        song_string = file.read()
        return song_string

def _split_song_string(song_string):
    string_array = re.split(r'[\n]{2,}', song_string)
    return string_array

extension_map = {
    "txt" : _read_txt_file,
    "docx" : _read_txt_file
}