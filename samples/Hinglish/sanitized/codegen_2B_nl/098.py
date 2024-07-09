
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """
    s = s.upper()
    indices = [i for i, k in enumerate(s) if k not in 'aeiou']
    count = sum(c == 'a' for c in indices)
    return count
