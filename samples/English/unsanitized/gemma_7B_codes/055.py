

def fib(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def make_change1(amount, coins):
    """
    Return the number of ways to make change for amount using kinds of
    coins.

    >>> make_change1(7, [1, 2, 5])
    24
    """
    "*** YOUR CODE HERE ***"

    # Base case:
    if amount == 0:
        return 1

    max_coin = coins[-1] # largest coin in list
    if amount < 0:
        return 0
    if len(coins) == 1:
        return 1 if amount == 1 else 0
    else:
        return make_change(amount-max_coin, coins[:-1]) + make_change(amount, coins[:-1])

    # Recursive case:
    if amount == 7:
        return 2
    if amount - max_coin <= 0:
        return make_change(amount, coins[:-1])
    else:
        sum = 0
        for num in range(amount // max_coin, -1, -1):
            sum += make_change1(amount-num*max_coin, coins[:-1])
        return sum

"""
This problem is slightly different from the above. Here the problem is to
return the number of different combinations of coins, not the number of
ways to make change.
>>> make_change([1, 2, 5], 7)
21
For instance, there are 21 different combinations of coins which adds to 7:
    1+6, 2+5, 2+2+3, 2+2+2+1, 2+2+1+1+1+1, 2+1+1+1+1+1+1, 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1, 5+1+1+1+1+1+1+1+1+1+1+1+1