import damerau_levenshtein
import pickle


class Dictionary:
    def __init__(self):
        self._local_dictionary = set()
        self._generate_local_dictionary()
        with open('dictionary.pickle', 'rb') as f:
            self.dictionary = pickle.load(f)
        self._max_number_differences = 3

    def _generate_local_dictionary(self):
        with open('russian.txt', encoding='utf-8') as f:
            for word in f:
                self._local_dictionary.add(word.rstrip('\n'))

    def check_word_in_dictionary(self, word):
        return word in self._local_dictionary

    def get_candidates(self, word):
        candidates = []
        stack = [self.dictionary[0]]
        while len(stack) != 0:
            current_node = stack.pop()
            dist = damerau_levenshtein.calculate_distance(current_node.val, word)
            if dist <= self._max_number_differences:
                candidates.append(current_node.val)
            for dist_child, number_next_node in current_node.children.items():
                if dist - self._max_number_differences <= dist_child <= dist + self._max_number_differences:
                    stack.append(self.dictionary[number_next_node])
        if len(candidates) == 1:
            return []
        return candidates
