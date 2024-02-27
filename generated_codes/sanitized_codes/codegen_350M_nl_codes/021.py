from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Diye gaye numbers ki list (kam se kam do elements ki) par ek linear transform apply karo,
    aisa ki sabse chota number 0 ban jaye aur sabse bada number 1 ban jaye
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    kk = lambda x: x[0], x[1], x[2]
    mk = lambda x: x[0] - x[1], x[2] - x[0]
    res, t = lambda x: x[0] ** 2 + x[1], x[2] ** 2 - x[1], x[2] ** 2.0
    kk(res, t)
    mk(res, t)
    res, t = kk(res, t)
    res, t = mk(res, t)
    res, t = res * t
    res, t = res / t
    res, t = res % t
    res, t = res / t / 2e3
    return res