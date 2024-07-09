

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if (n % 2 == 1):
        return n
    else:
        return (prime(n / 2) + prime(n / 2) * prime(n / 2 + 1)) / 2

# ==========================================================================
# main function
# ==========================================================================


if __name__ == "__main__":
    # generate test dataset from 10x1 array
    A = np.random.rand(10, 1)
    print("data is :", A[0])

    # get all numbers from fizz, fizz, fizz,... fizz,...
    b = np.zeros(np.arange(len(A)) + 1)
    b[0] = 11.0
    b = np.cumsum(b).tolist()

    print("b[0] =", b[0])
    print("data is :", A[0, 0:2] + 10)

    # make the sum-array which is a simple array of integers
    # this is easy to do just for 2x1 array:
    # A = np.zeros(A.shape)
    # b = np.arange(A.shape[0])
    # for i in range(len(b)):
    #     A = np.concatenate((np.ones((i + 1, 1)), A), axis=1)
    # print(len(A))
    # print(A.shape)
    # A = np.cumsum(A)
    # print(A.shape)

    # get the number of elements of 2, 3, 5,...
    A = np.zeros(A.shape[:1])

    # A = np.cumsum(A)
    # print(len(