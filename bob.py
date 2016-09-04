import unittest

def bob(string):
    count = 0
    
    start = 0 
    end = start + 3

    for i in range(0, len(string), 1):
        if string[start:end] == 'bob':
            count += 1

        start += 1
        end += 1

    return "Number of times bob occurs is: " + str(count)


class TestBob(unittest.TestCase):

  def test_string_one(self):
      self.assertEqual(bob('azcbobobegghakl'), 'Number of times bob occurs is: 2')

  def test_string_two(self):
      self.assertEqual(bob('bobobob'), 'Number of times bob occurs is: 3')

if __name__ == '__main__':
    unittest.main()
