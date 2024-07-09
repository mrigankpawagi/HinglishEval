

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return max(l, key=len)

if __name__ == '__main__':
    a = [10, 20, 30, 40]
    b = [9, 7, 10, -2, -6, 6, 9]
    c = [1, 2, 3, 4]
    d = [1.1, 2.5, 3.8, 4.1]
    e = [0.2, 0.5, 1.2, 2.5]
    print medians(a)
    print medians(b)
    print medians(c)
    print medians(d)
    print medians(e)

This is the output

Output

A:

This is a rather inefficient way of doing what you want so I'm not sure if this is what you wanted to be done (and I haven't tested it because I didn't completely understand your function's output). I had to replace all the variables with a for loop.
