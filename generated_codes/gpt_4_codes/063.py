```python
def fibfib(n: int):
    """
    FibFib number sequence ek sequence hai jo Fibbonacci sequence ke saman hai aur iska definition is prakar hai:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Kripya ek function likhe jo efficiently fibfib number sequence ka n-th element compute kare.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_sequence = [0, 0, 1]
        for i in range(3, n+1):
            fibfib_sequence.append(fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3])
        return fibfib_sequence[n]
```