
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """
    c = 0
    s_copy = s

    if len(s_copy) % 2 == 0:
        for index in range(0, len(s_copy), 2):
            if s_copy[index] in 'AEIOU':
                c += 1
    else:
        s = ''.join(s[i] for i in range(0, len(s) - 1))
        for index in range(0, len(s), 2):
            if s[index] in 'AEIOU':
                c += 1
    return c


if __name__ == "__main__":
    print(count_upper("abBcde"))
