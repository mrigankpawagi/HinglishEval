

def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    kwargs = re.findall('( \\*)(\\*)(?=\\* )(?=\\*)', string)
    if len(kwargs) == 0:
        string = ""
        for k in kwargs:
            string += k

    if len(string)!= len(kargs):
        string = string[: ] + kArgs
    return string
