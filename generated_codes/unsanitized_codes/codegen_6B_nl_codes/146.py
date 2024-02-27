
def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai 
    array ke kitne elements 10 se bade hai aur jinke 
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    filtered_array = []
    for number in nums: 
        if number % 10 == 1 or number % 10 == 3 or number % 10 == 5 or number % 10 == 7 or number % 10 == 9: 
            filtered_array.append(number)

    return len(filtered_array)

