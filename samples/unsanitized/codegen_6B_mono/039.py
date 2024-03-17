

def prime_fib(n: int):
    """
    prime_fib woh n-th number return karta hai jo ek Fibonacci number bhi hai aur prime number bhi.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    f = [2, 3]
    for i in range(2,n):
        f.append(f[-1] + f[-2])
    p=[]
    for num in f:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            p.append(num)
    return p[-1]

# =================== Python Lambda ====================

# x = lambda a, b: a * b
# print(x(3, 4))

# =================================

# 1. Find the sum of the first 10 even numbers.
# def sum_ten(n):
#     return sum(i for i in range(1, n) if i % 2 == 0)

# print(sum_ten(10))

# 2. Define a function make_list that can accept two arguments: a list_length and a starting number.
# Return a list of the starting number filled with that many list element.
# >>> make_list(3, 1)
# [1, 2, 3]
# >>> make_list(1, 2)
# [1, 2]
# >>> make_list(11, 2)
# [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# def make_list(list_length, number):
#     return [number for n in range(1,list_length)] 

# print(make_list(3, 1))
# print(make_list(1, 2))
# print(make_list(11, 2))

# 3. Find a function that takes two lists and returns the length of the intersection list.
