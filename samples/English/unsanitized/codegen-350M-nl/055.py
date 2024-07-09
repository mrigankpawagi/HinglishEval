

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = (f)
    result = -1
    n = n - a
    if n % 2 == 0:
        n += b
    n += b + b
    while n!= n + b:
        n -= b
    return n

In Python 1 only the multiplication operator (1 + 1)(2 + 1) will do. The addition of two numbers has already be converted to Fibonacci sequence by dividing an input by 2. 
Therefore, we can get the result directly by using the addition of a number 1 by an integer:
f = add(1, fib(int(f)))

Or, the same with (f) by fib(int(f)).
Notice that the Python representation of the Fibonacci sequence is already a valid one. Python's addition (x-1) is just the equivalent for any integer type, so it is also valid. It has a few flaws:

You need an implicit conversion.
x - 1 is a primitive number.

Both the addition of numbers 1 by number 2 is possible, but probably not desirable. 
1 + 1 has to be evaluated immediately before being added by adding numbers 1 + 1 to 1. 

A:

1 + 1 is a valid conversion to an integer. The other conversions to a valid integer are only done internally at compile-time if you define the return type to be Integer.
The addition of more than one number has two major flaws: if one of them is an integral part of the result, the result has to be an Integer.
1 + 2 has to be a Float type before evaluation of add when the result is Float, so at compile time you would have to perform an implicit conversion, to convert to the appropriate type.
Notice that the addition of two numbers on the same stack is also a valid conversion, it happens at the top-level of the stack so by definition the stack will carry the result of the stack