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
    def sum_up(in_arr):
        if not in_arr:
            return 0
        elif len(in_arr) == 1:
            return in_arr[0]
        else:
            return sum_up(in_arr[:]) + sum_up(in_arr[:])
    def sum_down(in_arr):
        if not in_arr:
            return 0
        elif len(in_arr) == 1:
            return in_arr[0]
        else:
            return sum_down(in_arr[:]) + sum_down(in_arr[:])
    return sum_up(in_arr) - sum_down(in_arr)