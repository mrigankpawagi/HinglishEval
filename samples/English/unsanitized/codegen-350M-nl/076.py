
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
    return is_simple_power(n, len(x)) == len(x)

    def f_simple_expand_left(x):
        """Your task is to write a function that returns the inverse of a simple
        power x, that is, when x is power of n, returning a new simple power which is
        the inverse of x
        """
        if n%len(x) :
            return x[0]
        else:
            return x[1:]

    def f_simple_expand_right(x):
        """Your task is to write a function that takes x as its input and returns a new
        simple power x.
        The input can be a power of n
        """
        return x[:-1]

    def f_simple_expand_right_left(x):
        """Your task is to write a function that takes x as its input and returns a new
        simple power x.
        The input can be a power of n
    