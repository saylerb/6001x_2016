import unittest

from deep_flatten import flatten

class FlattenTest(unittest.TestCase):
    def test_case_one(self):
        expected = [1,'a','cat',2,3,'dog',4,5]
        result = flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
