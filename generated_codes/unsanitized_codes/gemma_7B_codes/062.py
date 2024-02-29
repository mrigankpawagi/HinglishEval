def derivative(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * xs[i] for i in range(1, len(xs))]


def integral(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka integral same form mein return karo.
    >>> integral([1, 2, 3])
    [0.5, 1, 1.5]
    >>> integral([1, 2, 3, 4, 5])
    [0.5, 1, 1.5, 2.5, 3.5]
    """
    return [i * xs[i] / (i + 1) for i in range(len(xs))]


def main():
    xs = [1, 2, 3, 4, 5]
    print(derivative(xs))
    print(integral(xs))


if __name__ == "__main__":
    main()
