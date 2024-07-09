
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # return len(string) // 2
    count = 0
    for i in xrange(len(s)):
        if s[i] == "A":
            count += 1

        if s[i] == "E":
            if i % 2: count += 1
            continue

        if (s[i] == "I" and i % 2) or (s[i] == "O" and i % 2):
            if i % 2: count += 1
            continue

        if s[i] == "U":
            if i % 2: count += 1

    return count

print("Before: {}".format(str(dict_of_chars[str("AEIOUZ")])))
print("After: {}".format(dict_of_chars["AEIOUZ"].count_upper()))
# After: 50000
# Before: 10000

