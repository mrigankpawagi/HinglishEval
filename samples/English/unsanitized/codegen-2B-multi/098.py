
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(len(s)):
        if s[i] is 'B' and s[i+1] is (1 if i % 2 == 0 else 'b'):
            count += 1
    return count

# def word_count(s):
#     return len([c for c in s if c.isupper()])

