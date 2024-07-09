
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
        if i >= 0:
            count += 1
        else:
            count += 1 + abs(i)
    return count


assert count_nums([]) == 0
assert count_nums([-1, 11, -11]) == 1
assert count_nums([1, 1, 2]) == 3
