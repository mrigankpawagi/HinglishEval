import math


def poly(xs: list, x: float):
    """
    xs coefficients wale polynomial ko point x par evaluate karo.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Polynomial ko evaluate karta hai coefficients xs ke saath point x par.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    res = poly(xs, 0)
    if res == 0:
        return xs

    if res > 0:
        return find_zero([0] + xs)
    else:
        return find_zero(xs[:-1])


def find_root(
    xs: list,
):
    return poly(xs, find_zero(xs))


if __name__ == "__main__":
    print(find_zero([1, 0, 0, -3, 5, 3, -9, 1]))
