

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if (n == 0):
        return 0
    num = 0
    while (n!= 0):
        num += n
        n -= 1
    return num

if __name__ == '__main__':
    print(sum_to_n(5))
    print(f'Sum is {sum_to_n(100)}')

I did it so many times that I don't even remember how to do it. Thanks a lot for all your help.

A:

You can change your sum_to_n function so that it returns sum to n instead.
