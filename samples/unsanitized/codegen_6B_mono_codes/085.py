
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    temp = lst[1::2]
    temp.reverse()

    # lst[::2] lst[::2] even => odd
    return lst[0:1] + temp + lst[2::2] + lst[3::2]

# a_list =[2, 3, 7, 4, 6, 9, 10, 1, 8, 5, 4, 2]
# print(add(a_list))

