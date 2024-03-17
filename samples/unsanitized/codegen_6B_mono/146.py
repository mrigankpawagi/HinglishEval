
def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai 
    array ke kitne elements 10 se bade hai aur jinke 
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    sF = []
    for n in nums:
        if n%10 ==1 or n%10==3 or n%10==5 or n%10==7 or n%10==9:
            sF.append(n)
    print sF
            
