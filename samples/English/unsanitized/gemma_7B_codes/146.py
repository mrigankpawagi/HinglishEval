
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
    for x in nums:
        temp = x
        if(x < 10):
            continue
        while(x > 0):
            if(x%10 not in [1,3,5,7,9]):
                break
            x //= 10
        if(x > 0):
            count += 1
        
    return count
