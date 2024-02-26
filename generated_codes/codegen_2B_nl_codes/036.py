

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
    return (n - 1) / 7 - 1 or 1

So you are checking if every digit in the string is divisible by 7.
Now you are just a little unsure of how you are going about this. If you want to change the function so that your error handling only occurs when your code doesn't do what it should, add a return statement after that if.
