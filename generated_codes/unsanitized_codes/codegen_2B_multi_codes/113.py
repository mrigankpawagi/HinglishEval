
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    if not lst: return []
    in_ = ""
    for i, n in enumerate(lst[0]):
        if n in "0123456789":
            in_ += str(i)
    s = in_.replace("0", "n")
    print s
    odds = ""
    for i, n in enumerate(s):
        if n.isnumeric() and (n - int(n)) % 2 == 0:
            odds += str(i + 1)
    res = ["the number of odd elements " + s]
    res.append(odds)
    res.append("nput.")
    return res
