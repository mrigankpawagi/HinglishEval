
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = ''.join(chop(i) for i in s)
    result = 0
    for i in range(1, len(s)):
        result += _is_upper(s[i])
    return result
    
# from https://stackoverflow.com/questions/25122351/tutorial-how-to-find-count-of-vowels
