
def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai 
    array ke kitne elements 10 se bade hai aur jinke 
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    return list(filter(lambda x: x < 0, filter(lambda x: any((x == 10, x % 2 == 1)) == False, nums[:])))


print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))

# Question 5
"""
Create a function which removes the duplicate element in a list and return a new list.
"""


