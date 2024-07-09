
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
    x_int = int(x)
    return x_int % n == 0


if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('true')
    print('Output :')
    print(is_simple_power(10, 10))

    print('Example 2:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('false')
    print('Output :')
    print(is_simple_power(0, 0))
    a = float(input())
    b = float(input())
    print(is_simple_power(a, b))
