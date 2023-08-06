import unittest
from dictionary import Dictionary


class DictionaryTest(unittest.TestCase):

    def test_check_word_in_local_dictionary(self):
        dictionary = Dictionary()
        in_dict = dictionary.check_word_in_dictionary('привет')
        not_in_dict = dictionary.check_word_in_dictionary('Программмтс')
        self.assertEquals(in_dict, True)
        self.assertEquals(not_in_dict, False)



if __name__ == '__main__':
    unittest.main()
