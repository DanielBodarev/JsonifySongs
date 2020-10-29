import re

class TextBlock:
    def __init__(self, text, regex="", default_symbol=""):
        self.text = text
        self.regex = regex
        self.symbol = default_symbol
        self._split_symbol_from_text()

    def _split_symbol_from_text(self):
        if self.regex:
            split_text = re.search(self.regex, self.text)
            if split_text:
                if split_text.group(1):
                    self.symbol = split_text.group(1)
                if split_text.group(2):
                    self.text = split_text.group(2)

    def __str__(self):
        if self.symbol:
            return "{} {}".format(self.symbol, self.text)
        return self.text