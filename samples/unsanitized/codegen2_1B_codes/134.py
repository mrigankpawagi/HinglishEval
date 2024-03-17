
def check_if_last_char_is_a_letter(txt):
    """
    Ek function banaiye jo True return kare agar diye gaye string ka last character ek alphabetical character ho aur wo kisi word ka hissa na ho, anyatha False return kare.
    Dhyan de: "word" ek characters ka group hota hai jo space se alag na ho.

    Udaharan:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("") ➞ False
    """
    try:
        if (len(txt) > 1) and (isalpha(txt[-1])):
            if ''.join(txt[:-1]) == ''.join(txt[0:-1]):
                return True
            else:
                return False
        else:
            return False
    except IndexError:
        return False


