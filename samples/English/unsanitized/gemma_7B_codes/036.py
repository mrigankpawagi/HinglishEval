

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
    total = 0
    a = list(map(lambda x: [int(y) for y in str(x)], range(1, n + 1)))
    for i in list(filter(lambda x: (x[0] + x[1]) % 11 != 0 and (x[0] + x[1]) % 13 != 0, a)):
        for j in list(map(lambda x: [i, int(x)], list(str(x)))):
            if j[0] == 7:
                total += 1
    return total

print(fizz_buzz(x))
