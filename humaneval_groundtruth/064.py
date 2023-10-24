
FIX = """
Add more test cases.
"""

def vowels_count(s: str):
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
    assert type(s) == str, "invalid inputs" # $_CONTRACT_$
    if s == "": return 0
    cnt = len(list(filter(lambda ch: ch in "aeiouAEIOU", s)))
    if s[-1] in "yY": cnt += 1
    return cnt

def check(candidate):

    # Check some simple cases
    assert candidate("abcde") == 2
    assert candidate("Alone") == 3
    assert candidate("key") == 2
    assert candidate("bye") == 1
    assert candidate("keY") == 2
    assert candidate("bYe") == 1
    assert candidate("ACEDY") == 3


check(vowels_count)