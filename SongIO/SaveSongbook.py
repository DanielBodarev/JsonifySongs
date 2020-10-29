from JsonUtils.JsonConverter import songbook_to_json_format

def save_songbook(songbook):
    path = songbook.get_json_path()
    json_string = songbook_to_json_format(songbook)
    with open(path, 'w') as outfile:
        outfile.write(json_string)