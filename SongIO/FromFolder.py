from SongIO import FromFile
from os import listdir
from os.path import isfile, join

def get_song_array_from_folder(path):
    file_array = _get_file_array_from_folder(path)
    song_array = [create_song_from_file(file) for file in file_array]
    return song_array

def _get_file_array_from_folder(path):
    file_array = [file for file in listdir(path) if isfile(join(path, file))]
    return file_array