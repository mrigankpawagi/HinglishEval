

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    lst = []
    lst.append(0)
    lst.append(0)
    lst.append(1)
    idx = 4
    while idx < n:
        lst.append(sum([lst[idx-4], lst[idx-3], lst[idx-2]]))
        idx += 1
        if idx > n:
            print(lst)
            break
            
    print(lst)
    return lst[n-1]
