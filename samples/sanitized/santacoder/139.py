
def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    jaha n > 0

    Jaise ki:
    >>> special_factorial(4)
    288

    Ye function ek integer input ke roop me lega aur is integer ka special
    factorial return karega.
    """    assert isinstance(n, int), "integer n expected for `n`"

    def aux(n):
        # base case : n = 1
        if n <= 0:  # n <= 0 => n ~= 0
            return 1

        # recursive case : n > 1
        return n * aux(n - 1)

    return aux(n)

