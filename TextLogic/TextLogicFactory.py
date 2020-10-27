import TextAnalyzer.TextPropertyChecker

class TextLogicFactory:

    def get_text_logic(self, song):
        checker = TextPropertyChecker(song)
        props = checker.get_text_properties()

