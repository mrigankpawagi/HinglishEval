
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    res = 0
    for index in range(1,len(lst),2):
        res += lst[index]

    return res




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def get_even_index_numbers(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. All even-indexed number ko list mai append karo.
    index 0 even hai, so list[0] should be included. index 1 odd hai, so list[1] should be excluded.

    return: list of all even-indexed number in lst
    Udaharan:
        get_even_index_numbers([1,2,3,4]) ==> [1, 3]
    """
    new_list = []
    for index in range(len(lst)):
        if (index % 2 == 0):
            new_list.append(lst[index])

    return new_list




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def get_odd_position_numbers(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. All numbers ko list mai append karo, but all in an odd position.

    index 0 odd hai, so list[0] should be included.
    index 1 even hai, so list[1] should be excluded. But list[2], index 2 odd hai, so included.
    and so on.

    return: list of all numbers in lst in odd positions
    Udaharan:
        get_odd_position_numbers([1,2,3,4]) ==> [1, 3, 4]
    """
    new_list = []
    for index in range(len(lst)):
        if (index % 2 != 0):
            new_list.append(lst[index])

    return new_list




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #