import unittest

def alphaSub(string):

  current = string[0]
  longest = string[0]
  
  start = 0
  end = 1
  
  for i in range(0, len(string)- 1, 1):
  
      if string[start] <= string[end]:
          current += string[end]
  
      else:
          current = string[end]
  
      if len(longest) < len(current):
          longest = current
        
      start += 1
      end += 1
  
  return 'Longest substring in alphabetical order is: ' + longest


class TestAlpha(unittest.TestCase):

  def test_string_one(self):
      self.assertEqual(alphaSub('azcbobobegghakl'),
        'Longest substring in alphabetical order is: beggh')

  def test_string_two(self):
      self.assertEqual(alphaSub('abcbcd'),
        'Longest substring in alphabetical order is: abc')

  def test_string_three(self):
      self.assertEqual(alphaSub('abcdefghijklmnopqrstuvwxyz'),
        'Longest substring in alphabetical order is: abcdefghijklmnopqrstuvwxyz')


if __name__ == '__main__':
    unittest.main()
