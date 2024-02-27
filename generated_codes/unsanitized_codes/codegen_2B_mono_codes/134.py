
def check_if_last_char_is_a_letter(txt):
    """
    Ek function banaiye jo True return kare agar diye gaye string ka last character ek alphabetical character ho aur wo kisi word ka hissa na ho, anyatha False return kare.
    Dhyan de: "word" ek characters ka group hota hai jo space se alag na ho.

    Udaharan:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("") ➞ False
    """
    # return True if txt[-1].isalpha() else False
    return txt!= "" and txt[-1].isalpha()

"""
Write a Python function to find a string value in a given string where the substring size can be 1 or 2. 
Sample function and result :

find_substring("The given string ", 3) ➞ "No match"
find_substring("The given string ", 2) ➞ "Match"
find_substring("The given string ", 1) ➞ "No match"
find_substring("The given string ", 0) ➞ ""


"""
