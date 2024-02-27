
def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    sorted_nums_list = sorted(nums)
    sorted_nums_list.append(sum(nums))
    print(sorted_nums_list)
    return sorted_nums_list

print(order_by_points([2, 0, -5, -13, 9, 9, 9]))

'''
>>> order_by_points([2, 0, -5, -13, 9, 9, 9])
[-5, -13, 2, 0, 9, 9, 9]
'''