

def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    val = int(string)
    if val < 0:
        val = -val
    if val == 0:
        val = -(int(string)/len(string))
    return val


@pytest.mark.xfail
