

def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    d = n
    t1 = d
    while (d%2 == 0):
        t1 = t1-2*d
        d = n

    if(t1%2!= 0):
        return largest_divisor(t1)
    else:
        return largest_divisor(n/t1)
