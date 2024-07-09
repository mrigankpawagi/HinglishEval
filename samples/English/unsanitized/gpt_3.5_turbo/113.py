def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements in the string 4 of the input."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements in the string 1 of the input.",
     "the number of odd elements in the string 8 of the input."]
    """
    result = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 != 0:
                count += 1
        result.append("the number of odd elements in the string {} of the input.".format(count))
    return result