from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    # your code here
    if strings:
        longest = ''
        for x in strings:
            longest_x = len(x)
            if longest_x > len(longest):
                longest = x
    if not strings:
        return None
    return longest


def longest2(strings: List[str], limit_count = 1):
  """
  Out of list of strings, return the longest one. 
  Return the first one in case of multiple
  strings of the same length. Return None in case the input list is empty. 
  >>> longest2_test=[long("1"), long("2"), long("3"), long("4"), long("5"), "a", "aa", "aaa", None]
  >>> longest2_test
  ['1', '2', '2', '2', '3', 'a', 'xxx', 'xxx', 'None']
  >>> longest2_test2 = [long(), long('1'), long('2'), long('3'), long('4'), long('5'), 'a', 'aa', 'aaa']
  >>> longest2_test2
  [None, '1', '2', '3', '4', '5', 'a', 'xxx', 'xxx']
  >>> longest2_test3 = [long(), long('', limit_count), long('1'), long('2'), long('3'), long('4'), long('5'), 'a', 'aa', 'aaa']
  >>> longest2_test3
  [None, '1', '2', '3', '4', '5', 'a', None, None, None]

  >>> longest2_test4 = ['c', 'c', 'a']
  >>> longest2_test4
  ['c', None, None]
  >>> longest2_test5 = ['', 'a', 'b', 'c', '', 'a', 'b', 'c']
  >>> longest2_test5
  ['c', None, None]

  >>> longest2_test6 = ['c', '', '', 'a', '', '', '', 'a', 'b', 'c', 'c']
  >>> longest2_test6
  ['c', None, 'a', None, None, 'a', 'b', 'c', 'c']
  