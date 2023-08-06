import unittest
import damerau_levenshtein as dl


class DamerauLevenshteinTests(unittest.TestCase):

    def test_same_line(self):
        self.assertEquals(dl.calculate_distance('лучший', 'лучший'), 0)

    def test_character_replacement(self):
        self.assertEquals(dl.calculate_distance('кот', 'ток'), 2)

    def test_character_permutation(self):
        self.assertEquals(dl.calculate_distance('прикол', 'рпикол'), 1)

    def test_character_skip(self):
        self.assertEquals(dl.calculate_distance('стжровак', 'стажировка'), 3)

    def test_empty_string(self):
        self.assertEquals(dl.calculate_distance('', 'разработчик'), 11)


if __name__ == "__main__":
    unittest.main()
