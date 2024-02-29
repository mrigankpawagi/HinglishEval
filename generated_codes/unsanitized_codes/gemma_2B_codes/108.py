def count_nums(arr):
    """
    Ek function likho count_nums jo ek array of integers leta hai aur return karta hai
    un elements ki sankhya jinka digits ka sum > 0 hota hai.
    Agar koi number negative hai, to uska pehla signed digit negative hoga:
    jaise ki -123 ke signed digits hote hai -1, 2, aur 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count


# print(count_nums([1, 1, 2]))
# print(count_nums([-1, 11, -11]))
# print(count_nums([1, 1, 2, 3, 4, 5]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
# print(count_nums([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1
