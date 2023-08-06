from pathlib import Path
from dictionary import Dictionary
from string import punctuation


class FileSpellchecker:
    def __init__(self, path):
        self.dictionary = Dictionary()
        self.path = path

    def get_options(self):
        with open(Path.cwd() / self.path, 'r', encoding='utf-8') as f:
            options = dict()
            for text in f:
                words = text.translate(str.maketrans('', '', punctuation)).split()
                for word in words:
                    if not self._is_number(word) \
                            and not self.dictionary.check_word_in_dictionary(word):
                        options[word] = self.dictionary.get_candidates(word)
            return options


    def _is_number(self, word):
        try:
            float(word)
            return True
        except ValueError:
            return False

