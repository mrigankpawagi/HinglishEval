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

    # kasuha jo eger isi kare
    # kare hai kao hai kisya!
    res = 0
    n = 0

    # 0
    if n == 0:
        res += 1
    # 1
    elif n % 2 == 0:
        res += n * fib4(1)
    # 2
    else:
        # print(n, " ishari ya seba!...")
        res += n * fib4(2 * n - 2)
    # 3
    n = n // 2

    if n != 0:
        res += fib4(n)  # fib4(0) -> 0

    return res
