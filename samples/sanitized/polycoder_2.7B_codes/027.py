def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.lower()
    string = string.split(" ")
    return string[0].lower().strip() + string[1].strip().lower() + string[2].strip()
