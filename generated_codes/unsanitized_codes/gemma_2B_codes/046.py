

def fib4(n: int):
    """
    Fib4 number sequence ek sequence hai jo Fibbonacci sequence ke saman hai, jo is prakar se define kiya gaya hai:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Kripya ek function likhe jo efficiently fib4 number sequence ka n-th element compute kare. Recursion ka use na kare.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)


def fib5(n: int):
    """
    Fib5 number sequence ek sequence hai jo Fibbonacci sequence ke saman hai, jo is prakar se define kiya gaya hai:
    fib5(0) -> 0
    fib5(1) -> 0
    fib5(2) -> 2
    fib5(3) -> 0
    fib5(n) -> fib5(n-1) + fib5(n-2) + fib5(n-3) + fib5(n-4).
    Kripya ek function likhe jo efficiently fib5 number sequence ka n-th element compute kare. Recursion ka use na kare.
    >>> fib5(5)
    4
    >>> fib5(6)
    8
    >>> fib5(7)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib5(n-1) + fib5(n-2) + fib5(n-3) + fib5(n-4)


def fib6(n: int):
    """
    Fib6 number sequence ek sequence hai jo Fibbonacci sequence ke saman hai, jo is prakar se define kiya gaya hai:
    fib6(0) -> 0
    fib6(1) -> 0
    fib6(2) -> 2
    fib6(3) -> 0
    fib6(n) -> fib6(n-1) + fib6(n-2) + fib6(n-3) + fib6(n-4).
    Kripya ek function likhe jo efficiently fib6 number sequence ka n-th element compute kare. Recursion ka use