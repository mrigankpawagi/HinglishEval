import math


def sum_squares(lst):
    return sum([math.ceil(i) ** 2 for i in lst])
