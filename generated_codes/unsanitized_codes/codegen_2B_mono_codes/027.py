

def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    lower = str.lower(string)  # Obeji string lekar nahi abhi
    upper = lower.upper()  # karle baad jayega bhi lower case ke bhi upper case ko ugula hoga
    return upper
