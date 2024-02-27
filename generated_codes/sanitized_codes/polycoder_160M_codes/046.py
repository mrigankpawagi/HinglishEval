

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
    def fib5(n: int):
        """
        Fib5 number sequence em se elementiske numeriske se defrata se eiksa reik se defrata kare. Recursion se use na kare.
        >>> fib5(n)
        8
        >>> fib5(n-1)
        3

        """
        def fib6(n: int):
            """
            Fib5 number sequence em se elementiske numeriske se defrata se eiksa reik se defrata kare. Recursion se use na kare.
            >>> fib5(n)
            6
            >>> fib5(n-5)
            8
            >>> fib5(n-2