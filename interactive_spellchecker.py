from dictionary import Dictionary
from string import punctuation


class InteractiveSpellchecker:
    def __init__(self, text):
        self.dictionary = Dictionary()
        self.list_words = text.split()

    def get_options(self):
        options = dict()
        for word in self.list_words:
            word = word.rstrip('\n').translate(str.maketrans('', '', punctuation))
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
