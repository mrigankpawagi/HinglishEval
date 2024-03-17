

def fib(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fibonacci(int))
    print(fibonacci(string))

A:

I recommend not using global vars
f_array = []
f_array.append(0)
f_array.append(1)

for i in range(20):
    f_array = [f_array[0],f_array[1],f_array[2]]    

