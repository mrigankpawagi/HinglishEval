

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

main()

Thanks in advance.

A:

The function largest_divisor is always going to return a number that is odd.
Your only condition to stop this happening is if n is divided evenly, but you only ever check if n % 2 == 0.
Instead of checking this you should just set n = (n + d - 1) / 2, where d is the odd number. This will ensure that n is even.

A:

largest_divisor will return a number that's divisible by 2, but will be even for even numbers.
Here's a simpler method:
