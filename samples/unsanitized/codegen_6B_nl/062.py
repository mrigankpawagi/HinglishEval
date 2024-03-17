

def derivative(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    poly = list(map(int, ''.join(map(str, xs)).replace(' ', '').split(',')))
    #print('poly', poly)
    poly = [p for p in poly]  # poly to integer
    poly.append(1)
    return poly


# >>> p = derivative(polynomials(0, 1, x - 3))
# [1, 4, 12, 20, 3] <<<
# polynomials ke polynomial ke coefficients ka derivative ko
#
# >>> p2 = derivative(polynomials(1, x + 1))
# >>> type(p2)
# <class 'list'>
