from Common.Settings import text as textSettings

word_limit = textSettings.getint('titlewordlimit', fallback=7)
char_limit = textSettings.getint('titlecharacterlimit', fallback=30)

def get_first_words_with_limits(text, wlimit=word_limit, chlimit=char_limit):
    text = str(text)
    split_text = text.split(" ")
    selected_text = _whittle_down_words(split_text, wlimit, chlimit)
    whittled_text = " ".join(selected_text)
    if len(whittled_text) > chlimit:
        whittled_text = whittled_text[:chlimit]

    return whittled_text

def _whittle_down_words(split_text, wlimit, chlimit):
    selected_text = split_text[:wlimit]
    total_size = _get_size_of_selected_text(selected_text)
    while total_size > chlimit:
        if len(selected_text) <= 1:
            break
        selected_text = split_text[:-1]
        total_size = _get_size_of_selected_text(selected_text)
    return selected_text

def _get_size_of_selected_text(selected_text):
    num_of_spaces = len(selected_text) - 1
    total = sum([len(word) for word in selected_text])
    return total + num_of_spaces