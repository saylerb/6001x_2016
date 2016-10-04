import unittest

from dictionary_diff import dict_interdiff

def add(a, b):
    return a + b

def greater(a, b):
    return a > b

class DictionaryDiffTest(unittest.TestCase):
    def test_case_one(self):
        d1 = {1:30, 2:20, 3:30, 5:80}
        d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

        expected = ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
        result = dict_interdiff(d1, d2, add)

        self.assertEqual(expected, result)

    def test_case_two(self):
        d1 = {1:30, 2:20, 3:30}
        d2 = {1:40, 2:50, 3:60}

        expected = ({1: False, 2: False, 3: False}, {})
        result = dict_interdiff(d1, d2, greater)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
