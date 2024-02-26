
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
    return int(x)*n==int(x)**int(n)

if __name__=="__main__":
    assert is_simple_power(2, 1) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(2, 3) == False
    is_simple_power(1, 4) == False
    is_simple_power(8, 2) == True
    is_simple_power(3, 2) == False
    is_simple_power(3, 1) == False
    is_simple_power(5, 3) == False
