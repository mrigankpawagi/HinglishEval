
def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai 
    array ke kitne elements 10 se bade hai aur jinke 
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    x = 0
    y = 0
    flag = 0 + x
    z = -y - (flags[y] or 1)
    #  check even and odd numbers and return even number

    if x > 10:
        x = 10
        flag = 1 + x

    while x < 10:
        try:
            if y == 0 and z > 0:
                # special filter function 1
                return (flags[y] and flags[y]) and (z or x)
            elif y == 1:
                # special filter function 2
                return (flags[y] or flags[y + 1]) and (z or x)
        except:
            break
        x += 1
    return 4
    specialFilter()

  