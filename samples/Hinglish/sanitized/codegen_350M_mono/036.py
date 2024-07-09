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
    def count(a: int):
        count = 0
        for i in range(1, 11, 1):
            if i % 7 == 0 and i % 2 != 0:
                count += 1
        if type(a) == int:
            return 0
        elif isinstance(a, str):
            return 0
        elif isinstance(a, list):
            return 0
        elif isinstance(a, dict):
            return 0
        else:
            return count
    count = count(n)
    def check(b, num):
        if any([num // i >= 3 for i in range(11)]):
            return "fizz"
        elif (num // 2 == 0) or (num // 3 == 0):
            return "buzz"
        else:
            return 0
    count = count % count
    count += 2
    # print(count)
    # print(check(num, count), num)
    if count == num:
        return "buzz" if num == count else "fizz"
    else:
        return "not buzz"