

def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not string:
        return 0
    return 1 + strlen(string[1:])


def str_reverse(string: str) -> str:
    """
    Diye gaye string ko reverse karo
    >>> str_reverse('')
    ''
    >>> str_reverse('abc')
    'cba'
    """
    if not string:
        return ''
    return str_reverse(string[1:]) + string[0]


# # 3
def list_append(a: list, b=None) -> list:
    """
    Diye gaye lists ko ek another ki length par append karna
    >>> list_append([])
    []
    >>> list_append([], [1, 2, 3])
    [1, 2, 3]
    >>> list_append([1, 2, 3])
    [1, 2, 3]
    >>> list_append([], [5, 6])
    [5, 6]
    >>> list_append([10], [20])
    [10, 20]
    """
    if b is None:
        return [a]
    return [a] + [b]


def list_reverse(a: list, b=None) -> list:
    """
    Diye gaye lists ka reverse kare
    >>> list_reverse([])
    []
    >>> list_reverse([1, 2, 3])
    [3, 2, 1]
    """
    if b is None:
        return [a]
    return [b] + [a]


def list_remove(a, d, n) -> list:
    """
    Diye gaye lists ki index mein aise diya gaya index ko remove kare
    >>> list_remove([], 0, 0)
    []
    >>> list_remove([1, 2, 3], 0, 0)
    [2, 3]
    >>> list_remove([1, 2, 3], 1, 0)
    [1, 3]
    """
    if a[n] == d:
        return a[0:n] + a[n + 1:]
    return