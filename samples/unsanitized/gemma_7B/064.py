FIX = """
Add more test cases.
"""


def vowels_count(s):
    """
    Aur test cases jodo.
    """
    return len([c for c in s if c in "aeiouAEIOU"])


if __name__ == "__main__":
    print(FIX)
    print(vowels_count("abracadabra"))
