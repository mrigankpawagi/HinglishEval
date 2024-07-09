def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join(
        random.SystemRandom()
        .choice([chr(i) for i in list(range(ord("a"), ord("z") + 1))])
        .upper()
        for i in string.lower()
    )