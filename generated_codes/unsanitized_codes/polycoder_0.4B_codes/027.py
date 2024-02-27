

def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for ch in string:
        if ch in string.upper():
            result += str(int(ch) - 26 * 'a') + str(int(ch) - 'E' + 1)
        else:
            result += str(int(ch) - 'a' + 1)
    return result[:-2]

