
def check_if_last_char_is_a_letter(txt):
    """
    Ek function banaiye jo True return kare agar diye gaye string ka last character ek alphabetical character ho aur wo kisi word ka hissa na ho, anyatha False return kare.
    Dhyan de: "word" ek characters ka group hota hai jo space se alag na ho.

    Udaharan:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("") ➞ False
    """    if len(txt) == 0:
        return False
    elif txt[len(txt) - 1] >= "0" and txt[len(txt) - 1] <= "9":
        return True
    else:
        return check_if_last_char_is_a_letter(txt[:-1])
