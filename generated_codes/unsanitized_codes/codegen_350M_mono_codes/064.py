
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    letter_count = len([letter for letter in s if (len(set(string.ascii_lowercase)) == 1) & (string.ascii_lowercase.index(letter) == string.ascii_lowercase.index(s[index]))])
    return f"{letter_count + 1}"
