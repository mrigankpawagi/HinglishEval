
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # Note: this function is written in such a hacky way to simplify: it
    # only works for values with more than two digits; then it should work for
    # those values it only calculates a factor of 10^(n) with integer powers
    # as input which can be checked by an integer in the range [1-10^16].
    # The main issue is that we loose the original result for special values.

    a = [1]
    for n in range(0, 2*int(round(math.log(n, 2.0)) + 1)):
        a.append(int(str(factorial(n)) + str(factorial(n - 1)) +
                str(factorial(n - 2))) * math.pow(10, n))

    # this is the biggest result from the above if, assume all the factors are
    # integer: 2^n * 3^n
    return (max(a) % 100) * math.pow(10, n + 1)

#
# Functions
#

