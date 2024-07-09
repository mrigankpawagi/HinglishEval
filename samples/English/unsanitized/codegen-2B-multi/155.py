
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return 0
    num_str = str(num)
    evens = 0
    odds = 0
    for i in range(len(num_str)):
        if num_str[i] % 2 == 0:
            evens += 1
        else:
            odds += 1
    return (evens, odds)


if __name__ == '__main__':
    import sys
    if (len(sys.argv) <= 1):
        print("usage: {} n".format(sys.argv[0]))
        sys.exit(1)
    n = int(sys.argv[1])
    print("{}".format(even_odd_count(n)))