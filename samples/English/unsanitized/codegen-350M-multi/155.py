
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    evens = []
    odds = []
    for i in range(num):
        evens.append(i & 1)
        odds.append((i >> 1) & 1)
    evens = list(evens)
    odds = list(odds)
    return all(odds), evens


