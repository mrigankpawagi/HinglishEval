
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    vowels = ['a','e','i','o','u']
    vowel_counter = 0

    for vowel in vowels:
        vowel_counter += s.count(vowel)
    
    return vowel_counter

vowels_count("")

# print('vowels_count("") = ', vowels_count(""))
# #>>> vowels_count("") = 0

# print('vowels_count("") = ', vowels_count("aeiou"))
# #>>> vowels_count("aeiou") = 3