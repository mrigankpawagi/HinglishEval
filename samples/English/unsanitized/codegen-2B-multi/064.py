
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
    # This approach is not ideal for the exercise. There can be multiple paths
    # through the code to determine the status of a vowel. It could be: 
    # 1. the word begins with a vowel;
    # 2. the first letter of the word is "a", e"", "i", "o", or "u";
    # 3. the second letter is "a", e"", "i", "o", or "u";
    # (following that example, "abce" can't be a vowel.)
    count = 0
    for i in range(0,len(s)):
        if s[i] in "aeiou":
            count += 1
        elif i == len(s)-2 and s[i]+s[i+1] in "aeiou":
            count += 1
    return count

