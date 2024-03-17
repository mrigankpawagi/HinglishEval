def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai
    array ke kitne elements 10 se bade hai aur jinke
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    n = 0
    while len(nums) > n:
        num_jail = nums[n] * 0.1 + nums[n] / 1.08
        n += 1
        if num_jail in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            new = list(nums)
            new = [j for j, (num_jo) in zip(nums[:-1], new[0])]
            if len(new) == n:
                return new[n - 1]
    return nums
