def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai
    array ke kitne elements 10 se bade hai aur jinke
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    a = [int(i) for i in sorted(nums)]
    flag = False
    a, result = list(a), 0
    while a:
        temp = a[result]
        if temp == 9:
            k = a.pop(result)
            b = 0
            while k != 9:
                result += 1
                b = 1
                k = a[b]
            if not b:
                k = sorted(nums)
                k[sorted(k)].append(k[sorted(k)].pop(0))
                nums.append(k)
                result = 1
                flag = True
            a.pop(result - 1)
        elif (
            temp == 2 or temp == 3 or temp == 6 or temp == 7 or temp == 5 or temp == 19
        ):
            k = a.pop(result)
            b = 0
            while k != 9:
                result += 1
                b = 1
                k = a[b]
            if not b:
                k = sorted(nums)
                k[sorted(k)].append(k[sorted(k)].pop(0))
                nums.append(k)
                result = 1
                flag = True
            a.pop(result - 1)
        try:
            nums[result] = next(filter(lambda x: x == temp, nums))
        except:
            nums = list(filter(lambda x: x == temp, nums))
        if not a:
            break
    return flag