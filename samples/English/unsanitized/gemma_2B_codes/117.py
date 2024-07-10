
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # YOUR CODE HERE
    # check if the string is empty and return an empty list if true
    if len(s) == 0:
        return []
    # get a list containing the consonants
    consonants = [c for c in "abcdefghijklmnopqrstuvwxyz"]
    # go through each letter in the string
    for i in range(0, len(s)):
        # if that letter is not a consonant
        if s[i] not in consonants:
            # append the letter to the list
            s = s[:i] + s[i+1:]
    # return the list of all words from string s that contain exactly n consonants, in order these words appear in the string s
    return sorted(s.split())



## -------------------------


# TESTS
import unittest

class TestSelectWords(unittest.TestCase):
  def test1(self):
    self.assertEqual(
      [ 'little' ],
      select_words("Mary had a little lamb", 4)
    )

  def test2(self):
    self.assertEqual(
      [ 'Mary', 'lamb' ],
      select_words("Mary had a little lamb", 3)
    )

  def test3(self):
    self.assertEqual(
      [ ],
      select_words("simple white space", 2)
    )

  def test4(self):
    self.assertEqual(
      [ 'world' ],
      select_words("Hello world", 4)
    )

  def test5(self):
    self.assertEqual(
      [ 'Uncle' ],
      select_words("Uncle sam", 3)
    )   


if __name__ == '__main__':
  unittest.main(verbosity=2)
