
def is_sorted(lst):
    """
    Ek numbers ki list di gayi hai, return karo ki kya ye ascending order mein sorted hai ya nahi. Agar list mein ek se jyada same number ke duplicate hain, to False return karo. Maan lo ki koi negative number nahi hai aur sirf integers hain.

Udaharan
is_sorted([5]) ➞ True
is_sorted([1, 2, 3, 4, 5]) ➞ True
is_sorted([1, 3, 2, 4, 5]) ➞ False
is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    """
    seen = [-1]
    sorted_list = []
    for el in lst:
        seen[el] += 1
        if seen[el] > seen[seen[0]]:
            sorted_list.append(el)
    return len(sorted_list) == len(lst)

if __name__ == '__main__':
    s = sorted([1, 2, 3, 4, 5], reverse=True)
    sorted([1, 2, 3, 4, 5]) == [5, 1, 4, 3, 2]
    sorted_list = sorted((5, 1, 5), reverse=True)
    sorted_list = sorted([2, 4, 1], reverse=False)
    print(is_sorted(sorted_list))
    print(is_sorted([1, 2]))
    print(is_sorted(sorted_list[0]))
    print('Error', Exception(), len(sorted_list))
