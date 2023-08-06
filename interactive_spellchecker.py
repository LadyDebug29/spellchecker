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
            if not self.dictionary.check_word_in_dictionary(word):
                options[word] = self.dictionary.get_candidates(word)
        return options
