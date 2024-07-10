
def sorted_list_sum(lst):
    """
    Ek function likho jo strings ki list ko parameter ke roop mein accept karta hai,
    usme se odd lengths wale strings ko delete karta hai,
    aur resulted list ko sorted order mein return karta hai,
    List hamesha strings ki list hoti hai aur kabhi numbers ki array nahi hoti,
    aur usme duplicates ho sakte hain.
    List ka order har word ki length ke hisaab se ascending hona chahiye, aur aapko
    us rule ke hisaab se list ko sorted return karna chahiye.
    Agar do words ki length same ho, to list ko alphabetically sort karo.
    Function ko sorted order mein strings ki list return karni chahiye.
    Aap maan sakte ho ki sabhi words ki length same hogi.
    Jaise ki:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    return [j for i, j in enumerate(sorted(lst, key=lambda x: (-len(x), x))) if len(j) % 2 == 1]


# Q11
# write your code here


# Q12 :
# Write your code here.
def sorted_list(lst):
    return [i for i in sorted(lst) if i % 2 == 1]

    # # Solution #1:
    # lst_2 = [i for i in lst if len(i) % 2 == 1]
    # return lst_2

    # #Solution #2:
    # lst_2 = []
    # for i in lst:
    #     if len(i) % 2 == 1 :
    #         lst_2.append(i)

    # return lst_2

# Q13:
def list_intersection(lst_1, lst_2):
    return [i for i in lst_1 if i in lst_2]


# Q14


def list_intersection(lst_1, lst_2):
    pass

    return [i for i in lst_1 if i in lst_2]


# Q15
# def product(lst):
#     return prod([item for item in lst if isinstance(item, int)])


# def prod(lst):
#     res = 1
#     for i in lst:
#         res *= i
#     return res

# def product(lst):
#     return reduce(lambda a, b: a * b, lst)

from functools import reduce

def product(lst):
    return reduce(lambda a, b: a * b, [item for item in lst if isinstance(item, int)])


# Q16
def min_from_list(input_lst):
    min = min(input_lst)
    return min


# Q17
def min_from_list(input_lst):
    min = None
    for element in input_lst:
        if isinstance(element, int):
            if min is None or element < min:
                min = element
    return min

# def min_from_list(input_lst):
#     return min([element for element in input_lst