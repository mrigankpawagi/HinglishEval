

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    d, r = divmod(n, 2)
    while d is not 1:
        d, r = divmod(r, 2)
        if d < 1:
            break
    while r!= 0:
        d, r = divmod(r, d) if d!= 1 else (1, 0)
    print("Largest Divisor:", r)
    return r

if __name__ == "__main__":
    # tests for this function
    tests = [56400, 1, 2]
    for test in tests:
        print(largest_divisor(test))
