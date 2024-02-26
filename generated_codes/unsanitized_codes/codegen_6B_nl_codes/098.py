
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    vowels_upper = []
    for letter in s:
        if letter.isupper():
            vowels_upper.append(letter)
        else:
            vowels_upper.append(letter.lower())
    vowels_upper = tuple(vowels_upper)

    if vowels_upper in s:
        return vowels_upper.count(s)
    else:
        return 0

