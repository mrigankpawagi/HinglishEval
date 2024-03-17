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
    return poly(xs, 0)


def factorial(n):
    """
    polynomial ko evaluate karta hai n par integer 
    sayonar number n par integer polynomials ko generate wale polynomil
    sumator (wale) i.e. f(i) = x^i for integer i
    n par integer n par integer polynomials ko calculate wale poly(x^0 to x^i)
    sayonar number i par f(x) = i(x) * x^i for integer i
    """
    return math.prod([factorial(r) for r in range(n)])


def is_perfect(n: int):
    """
    Polynomial ko evaluate karta hai n par integer par integer polynomials ko 
    check the sumator (wale) i.e n par integer polynomials ko is the sumator 
    of wale polynomail ko is complete.
    """
    return factorial(n) == n * n * factorial(n-1)


def sum(xs: list):
    """
    Polynomial ko evaluate karta hai numbers par integer par integer polynomials ko 
    calculate sumation of numbers par integer par integer polynomials ko.
    Return sumator (wale) n par integer to integer to integers polynomial ko.
    """
    return sum([