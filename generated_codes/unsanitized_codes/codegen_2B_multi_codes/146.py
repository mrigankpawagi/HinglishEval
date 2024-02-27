def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai
    array ke kitne elements 10 se bade hai aur jinke
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    special_filter_arr = []
    for i in range(len(nums)):
        special_filter_arr.append(nums[i] >> 1)  # if 1 <>
        nums[i] = nums[i] - special_filter_arr.pop()  # -15 = 15-1
    return sum(special_filter_arr)
