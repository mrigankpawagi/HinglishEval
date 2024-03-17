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
    coeffs = [1] + list(xs)
    return reduce(lambda a, b: a - b, coeffs) / (pow(x, len(coeffs)) - 1)


def derive_coe(xs: list):
    """
    xs ko polynomial ko derivative find karta hai coefficients xs ke aap point.
    return [1] + xs[1] * x + xs[1 * x] * x^2+.... xs[n * x] * x^n, sum(ys)
    """
    return [1] + list(xs) + [reduce(lambda a, b: a * b, coeffs) * x for x in xs]


def integrate(xs: list, ys: list):
    """
    xs ko polynomial ko integrate karta hai ys point ko aap.
    return list of xs and value from 0 to xs[n] point.
    """
    a = [
        poly([1], x) - poly([1, 1], x) for x in range(0, len(xs))]
    b = [poly([1], x) - poly([1, 1, 1], x) for x in range(0, len(xs))]
    ys = list(zip(xs, ys))
    return zip(xs, [(a[i] / b[i]) * ys[i][1]