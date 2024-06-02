def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.
    Jaise ki:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    vowels = ["A", "E", "I", "O", "U"]
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count