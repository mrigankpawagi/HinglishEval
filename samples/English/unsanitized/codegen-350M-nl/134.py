
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
    newlen, char_to_skip=0, _, character_to_skip=0, _
    last_char=''
    for _ in txt:
        if _ == char_to_skip:
            if last_char == character_to_skip:
                char_to_skip=0
                last_char=text_to_skip(str(txt))
                if _ == character_to_skip:
                    newlen+=1
            if last_char == character_to_skip and newlen < last_char:
                return False
            chars_spaces_to_skip=0
            chars_to_skip=0
            last_char=character_to_skip
            last_char