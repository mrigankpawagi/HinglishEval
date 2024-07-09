
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    if txt[-1] is not None:
        # First character of a word is a character 
        # with a whitespace following it
                return False
        # Last character of an alphabetical group is not
        # followed by a non-alphanumerically character 
        # (e.g. "apple pie" was not "pi e"
        elif txt[-1:-1] not in [' ','']:
            # Last non-alphanumerically digit of an alphabetical group
            return True
            
    return False