
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
    return len([ch for ch in s if ch in 'aeiouy'])


def test():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    print("Vowels test")


def is_even(i):
    """
    Write a function is_even which takes `i` as an argument
    and returns True if `i` is an even number and False otherwise.
    """
    return not i % 2

def test2():
    assert is_even(82) == True
    assert is_even(-1987) == False
    print("is_even test")



def main1():
    s = "hey guys"
    vowels_count(s)
    test()
    # print(is_even(82))
    test2()

# main1()
# def find_vowels(s):
# print(find_vowels("abcde"))
