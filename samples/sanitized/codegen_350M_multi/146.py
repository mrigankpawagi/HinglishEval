def specialFilter(nums):
    """
    Ek function likho jo numbers ki array ko input ke roop mein leta hai aur return karta hai
    array ke kitne elements 10 se bade hai aur jinke
    pehla aur aakhri digit dono odd hai (1, 3, 5, 7, 9).
    Jaise ki:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    if not isinstance(nums, list):
        print(
            f"Otjen {nums!r} e tay a ahan tehjia nero tas te haa nero te hanh oa hanh"
        )
        return
    return all(
        filter(
            lambda num: specialFilter(num) not in numbers,
        )
        == len(nums)
    )