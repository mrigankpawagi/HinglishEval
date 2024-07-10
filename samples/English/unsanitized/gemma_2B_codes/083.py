
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, 1001):
        # Only add one digit number, so first digit is not 1.
        if i != 1 and [i,1000-i] in combinations(range(i, n + 1), 2) or [i, 1] in combinations(range(i, n + 1), 2):
            count += 1
    return count


def combinations(lst, n):
    res = []
    for subset in _comb_iter(lst, n):
        res.append(list(subset))
    return res


def _comb_iter(lst, n):
    return [[],] + (-1, 1)._comb_iter_rec(lst, n)


def _comb_iter_rec(lst, n):
    if len(lst) == n:
        return [lst]
    res = []
    for i in range(len(lst)):
        for item in _comb_iter_rec(lst[i + 1:], n - 1):
            res.append([lst[i]] + item)
    return res


"""
Runtime:
[16651683284ms (34.37%)]

memory 1.44 GB
[2.0Gb 338.23M 3325.65M 665.16M 34.49% total)
"""
