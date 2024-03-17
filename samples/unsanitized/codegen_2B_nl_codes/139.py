
def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    jaha n > 0

    Jaise ki:
    >>> special_factorial(4)
    288

    Ye function ek integer input ke roop me lega aur is integer ka special
    factorial return karega.
    """
    # n > 0
    # 1 <= n <= 25
    if int(n) >= 100:
        raise ValueError("n must be greater than 0 and less than 100.")

    if n == 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 1

    special_factorial_base = 2
    if int(n) >= 4:
        special_factorial_base *= special_factorial_base

    return int(special_factorial_base * (n - 1) * n)

# brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!

