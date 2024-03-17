def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.replace("-", "")
    string = string.replace("o-", "")
    string = string.replace("e-", "")
    return string