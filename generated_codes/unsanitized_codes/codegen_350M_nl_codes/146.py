
def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai 
    array ke kitne elements 10 se bade hai aur jinke 
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    for j, i in enumerate(nums):
        print("{0}: {1}".format(i, j))
    print(specialFilter(nums[i]))
    print(specialFilter(nums[-1]))
    print(specialFilter(nums[-3]))
    print(specialFilter([3]))
    print(specialFilter([-1, 22]))
    """
    print("{0}: {1}".format(i, 0))
    print("{0}: {1}".format(nums[-1], 32))
    print("{0}: {1}".format(nums[-3], 0))
    print("{0}: {1}".format(nums[-1], 22))
    print(specialFilter([6]))
    print(specialFilter([2]))
    print([i for i in set(nums) if i < 0] + set(nums[-i]))
    print([i for i in set(nums) if i > 0] + set(nums[-i]))
    print([i for i in set(nums) if i < 0] - set(nums[-i]))
    print([i for i in set(nums) if i > 0] + set(nums[-i]))
    print(specialFilter([12])) 
  