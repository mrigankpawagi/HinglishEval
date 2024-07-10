
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    return len(s) - s.replace("a", "").replace("i", "").replace("o", "").replace("u", "").replace("e", "")


# Write your main function here
def main():
    s = input("Enter a string:  ")
    number_of_vowels = vowels_count(s)
    string = f"'{s}' has {number_of_vowels} vowels."
    print(string)


# Do not change anything below
if __name__ == '__main__':
    main()
