

def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(string.lower().split()).replace(string, string.upper()).replace(string.upper(), string.lower()).lower()
