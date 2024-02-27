def check_if_last_char_is_a_letter(txt):
    """
    Ek function banaiye jo True return kare agar diye gaye string ka last character ek alphabetical character ho aur wo kisi word ka hissa na ho, anyatha False return kare.
    Dhyan de: "word" ek characters ka group hota hai jo space se alag na ho.
    Udaharan:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("") ➞ False
    """
    if len(txt) > 0:
        if txt[-1].isalpha():
            return True
        return False