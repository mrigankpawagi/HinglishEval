
def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai 
    array ke kitne elements 10 se bade hai aur jinke 
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    arr = []
    for n in nums:
        if n%2 == 0:
            arr.append(n)
    for i in range(len(arr)):
        if 2 in arr[i]:
            arr[i] = str(2)
            arr.append(arr[i])
    return "".join(arr)