
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """

    return (
        (s.count(i) for i in "aeioukc"),
        (s.count(i) for i in "bcdf"),
        (s.count(i) for i in "dbe"),
        
        (s.count('x') + s.count('c') + s.count('r')) // 2,  #