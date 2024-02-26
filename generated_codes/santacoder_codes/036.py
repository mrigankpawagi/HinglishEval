

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
    return [0,1,2,3,4,5,6,7,8,9][n%10] if n%3==0 and n%5==0 else [0,1,2,4,7,8,9][n%10]
