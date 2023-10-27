import multiprocessing
from concurrent.futures import ThreadPoolExecutor
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
                cpu_count = multiprocessing.cpu_count()
                with ThreadPoolExecutor() as executor:
                    count_parts_list = 1
                    if len(words) > cpu_count:
                        count_parts_list = len(words) // cpu_count + 1
                    start_ind_next_part = 0
                    length_part_list = len(words) // count_parts_list
                    for _ in range(count_parts_list):
                        for word, word_options in \
                                zip(words[start_ind_next_part:length_part_list],
                                    executor.map(self._get_options,
                                                 words[start_ind_next_part:length_part_list])):
                            if not word_options is None:
                                options[word] = word_options
                        start_ind_next_part += length_part_list
                        length_part_list += length_part_list

            return options

    def _get_options(self, word):
        if not word.isnumeric() \
                and not self.dictionary.check_word_in_dictionary(word):
            return self.dictionary.get_candidates(word)
