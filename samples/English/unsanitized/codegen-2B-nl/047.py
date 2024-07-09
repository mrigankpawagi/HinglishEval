

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    p = len(l) / 2
    return l[p] if len(l) % 2 else l[p] + 1

How to use the second function? We need to iterate twice until the list length passes odd, then we use the function directly and return the median. For the first solution, we need to pass the input list through the function twice, and then take the median:
if __name__ == '__main__':
    l = [1, 100, 10, 2, 25]
    med = median2(*l)
    print(med)

This will print 3.

One advantage of having a function that doesn't require the input list, that we can pass multiple inputs to: a list, tuple, generator expression, or even a list comprehension. 

