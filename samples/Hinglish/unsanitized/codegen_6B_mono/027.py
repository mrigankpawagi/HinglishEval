

def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    dictionary = {'upper':'lower', 'lower':'upper'}
    for key in dictionary:
        string = string.replace(key, dictionary[key])
    return string

# 2
