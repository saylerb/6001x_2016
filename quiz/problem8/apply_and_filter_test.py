import unittest

from apply_and_filter import applyF_filterG

def add_two(num):
    return num + 2

def greater_than_five(num):
    return num > 5

def greater_than_one_hundred(num):
    return num > 100

class ApplyAndFilterTest(unittest.TestCase):
    def test_case_one(self):
        L = [0, -10, 5, 6, -4]

        result = applyF_filterG(L, add_two, greater_than_five)

        self.assertEqual(6, result)
        self.assertEqual([5, 6], L)

    def test_it_can_handle_empty_list_after_filtering(self):
        L = [0, -10, 5, 6, -4]
        result = applyF_filterG(L, add_two, greater_than_one_hundred)

        self.assertEqual(-1, result)
        self.assertEqual([], L)


if __name__ == '__main__':
    unittest.main()
