from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Strings ki list ko ek single string mein jodo
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
