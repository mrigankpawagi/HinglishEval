
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
    """    if np.isscalar(n):
        raise TypeError('n must be scalar and is float!')
    n = np.atleast_2d(n)
    if n.length == 1:
        return 1 - n
    if n.size == 2:
        return n[0] * n[1]
    is_integer = (n.size == 3 and np.isnumeric(n[1]))
    n = n.astype(int) if is_integer else n
    if np.all(is_integer):
        return n**2
    res = np.sin(2 * np.pi * n / n[1])
    ztol = 0.1**8
    if not np.all(is_integer):
        ztol = np.exp(-2 * np.pi * ztol / n[np.logical_not(is_integer)])
    return res

