def odd_count(lst):
    result = []
    for i in lst:
        count = sum(1 for digit in i if int(digit) % 2 != 0)
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(count, count, count, count))
    return result