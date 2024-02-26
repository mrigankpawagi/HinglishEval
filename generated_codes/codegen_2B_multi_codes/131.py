
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return int((str(n).endswith('0')
                and ''.join(str(n)[::-1])) or
               '1'.join(str(n)[::-1])
              .split('0')[::-1][1:])

# Tests
assert digits(1) == 1, digits(1)
assert digits(4) == 0, digits(4)
assert digits(235) == 15, digits(235)
