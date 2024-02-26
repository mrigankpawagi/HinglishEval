
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    while num:
        num += num % 2
        yield 1,0


if __name__ == '__main__':
    import doctest
    (failure_count, test_count) = doctest.testmod()
    print(failure_count)
