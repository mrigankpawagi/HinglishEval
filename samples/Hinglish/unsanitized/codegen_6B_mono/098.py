
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """
 
    return sum(1 for i in s[:len(s)//2] if s[i].isupper())

count_lower = lambda b: sum(1 for y in b[len(b)//2:] if y.islower())
