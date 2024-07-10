

def get_positive(l: list):
    """
    List mein se sirf positive numbers return karo.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # positive list mein bhar lo
    positive = []
    # loop karo
    for num in l:
        # agar positive number hai, to yehi add karlo in positive list mein
        if num > 0:
            positive.append(num)

    # positive list ko yehi return karo
    return positive


def get_prime(l: list):
    """
    List mein se prime numbers return karo.
    >>> get_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [2, 3, 5, 7]
    >>> get_prime([17, 15, 11, 16, 5, 1, 3, 7, 13, 23, 29, 2, 0])
    [17, 11, 5, 3, 7, 13, 29, 2]
    >>> get_prime([-9, -1, 0, -23, 10, 2, 7])
    []
    """
    # prime list mein bhar lo
    prime = []
    # loop karo
    for num in l:
        # return false kar rahe hai, then isme isko add nahi karo
        if not is_prime(num):
            continue

        # yehi add karo unse list mein
        prime.append(num)
    # prime list ko return karo
    return prime


def is_prime(n: int):
    """
    >>> is_prime(1)
    False
    >>> is_prime(4)
    False
    >>> is_prime(8)
    False
    >>> is_prime(15)
    False
    >>> is_prime(97)
    True
    """
    # n ko 2 se le kar n - 1 tak jao
    for i in range(2, n):
        # i se divide ho raha hai
        if n % i == 0:
            return False

    # n 1 se divide nahi ho raha hai, and n ke upar ka range check nahi kar rhe hai.
    return True


