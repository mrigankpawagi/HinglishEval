

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count=0
    for i in range(1,n+1):
        y = i % 3
        if y==0:
            count=count+1
    if count >=1:
        print (f"{count}")
    else:
        print("we have this number")

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. CHECK YOUR RESULT IN A NOTE\n")
