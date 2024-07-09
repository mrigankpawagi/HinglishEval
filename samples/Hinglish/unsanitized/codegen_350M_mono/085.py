
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    print(lst)
    num = int(input("Enter number:\t"))
    if num < 2 or num > 29:
        print("Please enter an integer between 2 and 29.")
        add(lst)
    else:
        lst.append(num)
        print(add(lst))


# def remove(lst):
#     """
#     Ek non-empty list di gayi hai integers ki lst. Remove all even elements ko jo odd indices pe hai.
#             Eg. remove([8, 2, 4, 6, 7]) ==> [8, 2, 4]
#     """
#     print(lst)
#     print(lst.pop(8))
#     print(lst)
#     print(lst.replace(2, 9))
#     print(lst)
#
#
# def index_lst_even(lst):
#     """
#     Ek non-empty list di gayi hai integers ki lst. Get the index of even element wkite ko jo odd indices pe hai.
#                 Eg. index_lst_even([8, 2, 4, 6, 7]) ==> 8
#
#     """
#     print("Even element list:\t", lst)
#     print(lst.index(8))
#     print(lst[lst.index(8)])
#     print(lst[(lst.index(8))+1:])
#
#
# def min_odd_number(lst):
#     """
#     Ek non-empty list di gayi hai integers, list karo odd elements ko lai
#     get min odd element wkite ko de odd no ye hai
#
#     """
#     print("List karo odd elements\n", lst)
#     n = int(input("\nEnter minimum no