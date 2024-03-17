
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    count = 0
    for i in range(1, n+1):
        if i == 1 or i % 10 == 1:
            count += 1
    return count


# 2
def count_digits(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo.
    """
    count = 0
    for i in range(1, n+1):
        if len(str(i)) == n:
            count += 1
    return count


# 3
def count_digits_sum(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo sum of digits ke liye even hai.
    """
    count = 0
    for i in range(1, n+1):
        if sum(map(int, str(i))) % 2 == 0:
            count += 1
    return count


# 4
def count_digits_sum_even(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo sum of digits ke liye even hai.
    """
    count = 0
    for i in range(1, n+1):
        if sum(map(int, str(i))) % 2 == 0:
            count += 1
    return count


# 5
def count_digits_sum_odd(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo sum of digits ke liye odd hai.
    """
    count = 0
    for i in range(1, n+1):
        if sum(map(int, str(i))) % 2 == 1:
            count += 1
    return count


# 6
def count_digits_sum_even_odd(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo sum of digits ke liye even ya odd hai.
    """
    count =