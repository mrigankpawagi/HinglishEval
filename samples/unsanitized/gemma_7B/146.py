def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai
    array ke kitne elements 10 se bade hai aur jinke
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for i in nums:
        if i > 10 and i % 10 == 1 and i % 100 == 1:
            count += 1
    return count
