
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    odd_list = [x for x in range(10) if x % 2 != 0]
    even_list = [x for x in range(2, 10) if x % 2 == 0]
    even_list.sort()
    odd_list.sort(reverse = True)

    return even_list + odd_list

## another way
# import collections
# def even_odd_palindrome(n):
#     return collections.defaultdict(lambda: (0, 0))
#
#
# def f(odd_list, even_list):
#     odd_dict, even_dict = {}, {}
#     for i in odd_list:
#         key = i
#         odd_dict[key] = [i, i]
#     for i in even_list:
#         key = i
#         even_dict[key] = [i, i]
#     total = [odd_dict, even_dict]
#     for k, v in total:
#         for i in total[k].values():
#             v[i] += 1
#     return total
#
#
# def answer(n):
#     total = f(odd_list, even_list)
#     return total[0].keys()
#
#
# from collections import defaultdict
# from itertools import groupby
# odd_list = [x for x in range(10) if x % 2 != 0]
# even_list = [x for x in range(2, 10) if x % 2 == 0]
# even_list.sort()
# odd_list.sort(reverse = True)
#
# even_list = even_list[:n]
# odd_list = odd_list[:n]
# return defaultdict(lambda: (0, 0))
