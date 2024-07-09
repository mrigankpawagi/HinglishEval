

def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(string.lower().split()).replace(string, string.upper()).replace(string.upper(), string.lower()).lower()

if __name__ == '__main__':
    print(flip_case('This is a big string!'))

A:

I think splitting a string, creating a list, and joining the list again to get back the original string is a bit overkill. Just look for the first character to determine the case of the first letter:
