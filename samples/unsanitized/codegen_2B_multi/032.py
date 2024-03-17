import math


def poly(xs: list, x: float):
    """
    xs coefficients wale polynomial ko point x par evaluate karo.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Polynomial ko evaluate karta hai coefficients xs ke saath point x par.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    p = poly(xs, 1)
    ans = list(range(2 ** len(xs) - 1))
    for i in range(2 ** len(xs) - 1):
        x = 1 - (i - 1) / float(2 ** len(xs))
        ans[i * 2] = p - x * ans[int(i)] / 2
    return ans

def find_maxdiff(ys, xs):
    """
    Sets maximum diffrentiation of polynomial to 1 (if any) then set its maximum difference to xs.
    Args:
    ys(list of float) : The result of polynomial's evaluation fonctionnal ys
    xs(list of float) : The polynomial coefficients xs
    """
    ys_ = []
    for i in range(len(ys)):
        maxdiff = 1.0
        ys_a = ys[i]
        for j in range(i, len(ys)):
            if maxdiff < abs(ys[j]) - abs(ys_a):
                ys_a = ys[j]
                maxdiff = abs(ys[j]) - abs(ys_a)
        xs[i] += maxdiff * 2 - abs(ys_a)
    return xs

def get_range(xs: list, ys: list):
    """
    Return xs and ys with maximum difference.
    