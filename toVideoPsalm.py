import json
"""
with open('Speranta.json') as json_file:
    data = json.load(json_file)"""

class TextBlock:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class Verse (TextBlock):
    def __init__(self, text):
        super().__init__(text)

class Refren (TextBlock):
    def __init__(self, text):
        super().__init__(text)

class Song:
    def __init__(self):
        self.verses = []
        self.refren = []
        self.codas = []

    def add_verse(self, verse):
        self.verses.append(verse)

    def add_refren(self, refren);
        self.refren.append(refren)

    def add_coda(self, coda):
        self.codas.add(coda)

        
