
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    count = 0
    for letter in s:
        num_vowels = 1
        if letter == 'e':
            num_vowels = 2
        elif letter == 'y':
            num_vowels = ((count * 5)/2) + 1
        elif letter == 'a' or letter == 'i' or letter == 'o' or letter == 'u':
            continue
        else:
            raise ValueError("Unknown letter")
        count += num_vowels
    return count
