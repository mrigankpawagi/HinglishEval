
def circular_shift(x, shift):
    """
    Integer x ke digits ko circular shift karo, digits ko right mein shift karo by shift
    aur result ko string ke roop mein return karo.
    Agar shift > digits ki number ho, toh reversed digits return karo.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    result = s[len(s) - shift:] + s[0 : len(s) - shift]
    return result

# Question 2
def reverse_string(string):
    """
    String ki har letter ke opposite side ki letter ke pair mein dalo.
    >>> reverse_string("abcde")
    "decab"
    """
    for i in range(0, len(string)//2):
        string = reverse(string[i], string[-(i + 1)])
    return string

# Question 3
def reverse(s1, s2):
    """
    String s1 or s2 mein se ek string ke opposite side ki letter ke pair mein dalo.
    >>> reverse_string("abcde")
    "decab"
    """
    return s2 + s1

def is_vowel(x):
    """
    Boolean return karo ki kya character vowel hai.
    >>> is_vowel("c")
    None
    """
    vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for i in vowel:
        if i == x:
            return True
    return False

# Question 4
def is_pangram(x):
    """
    String mein har character ki present ho ya nahi ho use kar ke
    boolean return karo ki string pangram hai ka nahi.
    A pangram is a phrase or sentence that uses every letter of the alphabet.
    """
    pangram = {"A", "P", "N", "G", "R", "A", "M"}
    for i in x:
        if i in pangram:
            return False
    return True

# Question 5
def delete_string(string, index, length):
    """
    String mein se i jaise ke index se length tarah ke value delete karo.
    """
    return string[0:index] + string[index+length:]

# Question 6
def delete_last_char(x):
    """
    String mein last character remove karo.
    """
    x = x[:-1]
    return x

# Question 7
def delete_last