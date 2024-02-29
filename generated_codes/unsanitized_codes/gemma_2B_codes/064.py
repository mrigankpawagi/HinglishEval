FIX = """
Add more test cases.
"""


def vowels_count(s):
    """
    Aur test cases jodo.
    """
    return sum(1 for c in s if c in "aeiou")


def main():
    print(vowels_count(FIX))


if __name__ == "__main__":
    main()
