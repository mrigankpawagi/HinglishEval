
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if not n:
        return True
    # the problem here is very simple and easy to understand
    if n > 0 and x == int(x) and x**n == x:
        return True
    else:
        return False

# print(is_simple_power(1, 4))
# print(is_simple_power(2, 2))
# print(is_simple_power(8, 2))
# print(is_simple_power(3, 2))
# print(is_simple_power(3, 1))
# print(is_simple_power(5, 3))


