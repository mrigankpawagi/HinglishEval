from typing import List


def factorize(n: int) -> List[int]:
    """
    Diye gaye integer ke prime factors ki list return karo, order chhote se bade tak hona chahiye.
    Har ek factor ko utni baar list mein hona chahiye jitni baar wo factorization mein aata hai.
    Input number sabhi factors ka product hona chahiye
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    res = [int(x) for x in n]
    return OrderedDict(set(res))


class Factor(object):
    """
    The module handles conversion, factorization, and enumeration as simple operations.
    """
    def __init__(self, factors=None):
        self.factors = factors if factors is not None else []

    def __reduce__(self):
        return self.factors

    def __len__(self):
        return len(self.factors)


class Base(object):
    def __init__(self, factors=None, **kwargs):
        self.factors = factors if factors is not None else []
        self.kwargs = kwargs

    @classmethod
    def get_default_factors(cls):
        if cls is not Base:
            return cls.factors
        return set([self.factors])[0]

    def __reduce__(self):
        return self.factors

