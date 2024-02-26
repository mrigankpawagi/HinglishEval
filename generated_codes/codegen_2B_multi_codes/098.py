
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    i = 0
    while i < len(s):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            i += 1
        else:
            break
    return (len(s) - i) + (sum(1 for x in range(1, (i+1)) if s[x] == s[i]) % 2)


if __name__ == '__main__':
    # print(count_upper("aBCdEf"))
    # print(count_upper("abcdefg"))
    # print(count_upper("dBBE"))
    # print(' '.join(sorted(set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]))))
    print(count_upper("aBCdEf"))

