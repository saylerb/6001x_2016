import unittest
from time import sleep
from deep_reverse import deep_reverse_list

class DeepReverseTest(unittest.TestCase):
    def test_case_one(self):
        L = [[1, 2], [3, 4], [5, 6, 7]]
        deep_reverse_list(L)

        sleep(0.1)
        self.assertEqual([[7, 6, 5], [4, 3], [2, 1]], L)

if __name__ == '__main__':
    unittest.main()
