
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num <= 0 or num == 0:
        return 0, 0

    odd = num - (num % 10)
    if odd!= 0:
        return (5, odd)
    elif odd == 0:
        if num % 2!= 0:
            return (3, odd)
    elif odd!= 0:
        return (4, odd)
    else:
        return (False, 0)


