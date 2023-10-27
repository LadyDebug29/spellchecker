import multiprocessing
from dictionary import Dictionary
from string import punctuation
from concurrent.futures import ThreadPoolExecutor


class InteractiveSpellchecker:
    def __init__(self, text):
        self.dictionary = Dictionary()
        self.list_words = text.split()

    def get_options(self):
        options = dict()
        cpu_count = multiprocessing.cpu_count()
        with ThreadPoolExecutor() as executor:
            count_parts_list = 1
            if len(self.list_words) > cpu_count:
                count_parts_list = len(self.list_words) // cpu_count + 1

            start_ind_next_part = 0
            length_part_list = len(self.list_words) // count_parts_list
            for _ in range(count_parts_list):
                for word, word_options in \
                        zip(self.list_words[start_ind_next_part:length_part_list],
                            executor.map(self._get_options,
                                         self.list_words[start_ind_next_part:length_part_list])):
                    if not word_options is None:
                        options[word] = word_options
                start_ind_next_part += length_part_list
                length_part_list += length_part_list

        return options

    def _get_options(self, word):
        word = word.rstrip('\n').translate(str.maketrans('', '', punctuation))
        if not word.isnumeric() \
                and not self.dictionary.check_word_in_dictionary(word):
            return self.dictionary.get_candidates(word)
