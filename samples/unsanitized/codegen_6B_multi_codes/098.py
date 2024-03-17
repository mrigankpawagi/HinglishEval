
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """
    return sum([(ord(s[i]) >= ord(x)) and (ord(x) >= ord(s[i + 1]))
                for i, x in enumerate(s) if ord(x) >= ord('A') and i % 2!= 0])

