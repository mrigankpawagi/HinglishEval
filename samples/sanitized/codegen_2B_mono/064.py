FIX = """
Add more test cases.
"""


def vowels_count(s):
    """
    Aur test cases jodo.
    """
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = 0
    for vowel in vowels:
        vowel_counter += s.count(vowel)
    return vowel_counter