```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of the polynomial with coefficients xs using Newton's method.
    """
    def f(x):
        return poly(xs, x)
    
    def f_prime(x):
        return poly([i * coeff for i, coeff in enumerate(xs)][1:], x)
    
    x = 1.0
    while abs(f(x)) > 1e-6:
        x = x - f(x) / f_prime(x)
    
    return x
```