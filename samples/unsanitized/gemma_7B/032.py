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
    return poly(xs, x)


def find_root(xs: list, x_min: float, x_max: float, epsilon: float):
    """
    find_zero ko call karta hai.
    """
    x = (x_min + x_max) / 2
    while abs(find_zero(xs, x)) > epsilon:
        if find_zero(xs, x) * find_zero(xs, x_min) < 0:
            x_max = x
        else:
            x_min = x
        x = (x_min + x_max) / 2
    return x


def main():
    xs = [1, 2, 3, 4, 5]
    print(find_root(xs, 0, 10, 0.0001))


if __name__ == "__main__":
    main()
