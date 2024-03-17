
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """

    upper = 0
    for i in range(len(s)):
        if (ord(s[i])<97 or ord(s[i])>122) and (ord(s[i])>104 and ord(s[i])<110):
            upper = upper + 1
    return upper

# Naive Solution
