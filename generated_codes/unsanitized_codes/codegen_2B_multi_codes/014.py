from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    short = string[-1]
    long = ''
    prefixes = []

    for i in range(len(string) - 1, 0, -1):
        curr = string[:i]
        if curr == short:
            # this is a prefix of the current full string
            if long == '':  # the current prefix is the longest prefix
                prefixes = [short] + list(string[i+1:])
            short_again = string[i-1]
            while bool(prefixes) and short_again == prefixes[-1]:
                prefixes.pop()
                short_again = string[i-2]
                if short_again == prefixes[-1]:
                    # skip previous "a" before "a" with a
                    prefixes.pop()
            long += curr

    return prefixes


if __name__ == "__main__":
    import doctest
    doctest.testmod()
