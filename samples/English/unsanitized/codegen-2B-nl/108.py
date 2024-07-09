
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    n = len(arr);
    l = len(str(n));
    out = 0;
    for i in range(l):
        int_num = int(str(i), 10);
        if int_num > 0:
            out += 1;
    return out

print(count_nums([-123,-123,-123,-123,12,-123,-12,123,-12,-122,-122]))
print(count_nums([2,0,4,7,6,3,9]))
print(count_nums([3,4,100,34]))

A:

Well, you could do:
#!/usr/bin/env python

from __future__ import division

from builtins import map

_num = 1e300

