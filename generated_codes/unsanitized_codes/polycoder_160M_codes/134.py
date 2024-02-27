
def check_if_last_char_is_a_letter(txt):
    """
    Ek function banaiye jo True return kare agar diye gaye string ka last character ek alphabetical character ho aur wo kisi word ka hissa na ho, anyatha False return kare.
    Dhyan de: "word" ek characters ka group hota hai jo space se alag na ho.

    Udaharan:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("") ➞ False
    """

        if len(txt) == 0:
            return True

            #return False
        elif txt[0] == 'h' and not txt[-1] and len(txt) <= 3:
            return True

        return False

        '''
        Udaharan: Check if a char is the first occurrence of h in the last character of a string
        """
        '''
        duar :
        check_if_last_char_is_a_letter("apple palm") ➞ False
        check_if_last_char_is_a_letter("apple pia") ➞ False
        check_if_last_char_is_a_letter("apple pie") ➞ False
        check_if_last_char_is_a_letter("") ➞ False
        """        
        duar :
    