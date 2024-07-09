
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0, len(s), 2):
       if s[i].isupper():
           count += 1
    return count

   # ------------------------------------------------------------------
   # D. matching_char
   # Given a string of length 4, return a dictionary that contains
   #  the frequency of each letter in s
   #
   #  If e is not a letter, ignore it 
   #       and not count it
   #
   # Example: matching_char('ABC')
   # returns {'A': 2, 'C': 1, 'B': 2}
   #
  
   # ------------------------------------------------------------------
   # E. matching_char_dict
   # Given a string of length 4, return a dictionary that contains
   #  each letter as a key and its count stored as the value
       # If e is not a letter, ignore it 
       #       and not count it
   # Example: matching_char_dict('ABC')
   # returns {'A': 2, 'C': 1, 'B': 2}
   #
# ----------------------------------------------------------------------
