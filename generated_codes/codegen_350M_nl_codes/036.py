

def fizz_buzz(n: int):
    """
    n se kam integers mein, jo 11 ya 13 se divisible hain, usme digit 7 kitni baar aata hai, uska count return karo.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def zero(n: int):
        if n == 1:
            return 0
        zerolen = fizz_buzz(n - 1)
        if zerollen == 1:
            return zerolen
        zerolen = 2
        return zerolen + 1

    def funk(z: int):
        z = zerollen - 1
        while zerollen == 1:
            z = fizz_buzz(z)

        return z + 1

    def funk1(z: int):
        zerollen = fizz_buzz(z)
        while zerollen == zerolen:
            z = fizz_buzz(zerollen - 1)

        return z + 1

    def funk2(n: int):
        zerollen = fizz_buzz(n)
        while zerollen == 1:
            zerollen = funk(zerollen - 1)
        return zerollen + 1

    def funk3(n: int