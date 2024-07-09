
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    return int(round(value, 0)) if value!= str(int(value)) else int(value)

The problem is that if I pass a string containing a number like "14" it returns the integer 14. However, this problem doesn't occur when using the function "round".
Now the question, can we create a function that takes a number or string, but rounds towards zero and still return it?
Example
>>> closest_to_zero("10000.3")
1000.8    # Should return 1000.8 as there are 1000.8 numbers between two integers.
>>> closest_to_zero("-10000.3")
-1000.3   # Should return -1000.3 as there are -1000.3 numbers between two integers
>>> closest_to_zero("20000.3")
20000.3   # Should return 20000.3 as there are 20000.3 numbers between two integers
>>> closest_to_zero("19999.9")
19999.9   # Should return 19999.9 as there are not 19999.9 numbers between two integers

A:

Use round_down
I think what you are looking for is round_down.  It will return an integer but does rounding up
Example:
>>> def closest_integer(value):
    '''Create a function that takes a value (string)
    representing a number and returns the closest integer to