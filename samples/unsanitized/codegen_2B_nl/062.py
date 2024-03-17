

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

    if not xs:
        return []

    if len(xs) == 1:
        return [xs[0]]

    return zip(xs[:num], derivative(xs[len(xs):num]))

This function works with list where size is not fixed. 
In case of array is also fine.  
EDIT: I am expecting output when I give 1 as input it give me first derivative of polynomial(2,5,p)

A:

The easiest way is,
>>> def derivative(xs): 
...    if len(xs)<2:
...        return numpy.zeros(len(xs))
...    return [xs[i-1] for i in range(1, len(xs)+1)] + xx + [xs[0]]

In case of no value is not included,
the return is numpy.zeros(len(xs)).
For each xs[i-1], xx is returned.
And xx should contains all previous two values, xs[0] and xs[i].
See it work,
[] + [1, 1, 1] + [2, 3, 1]

The result is:
[[1, 1, 1, 0], [0, 2, 1], [1, 0, 1], [0, 1, 0]]

If your polynomial are a little complex, you can use itertools.
