

def get_positive(l: list):
    """
    List mein se sirf positive numbers return karo.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [i for i in l if i>0]

If I enter the input as [-2, 5, 6, 3, 2], I get the output as [6,2]. Could someone tell me what I'm doing wrong? I'm new to lists, and as far as I know, Python doesn't have any built in functions to find out if a list is positive.

A:

Simply use the bool operator:
