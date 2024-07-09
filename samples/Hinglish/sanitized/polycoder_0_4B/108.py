def count_nums(arr):
    """
    Ek function likho count_nums jo ek array of integers leta hai aur return karta hai
    un elements ki sankhya jinka digits ka sum > 0 hota hai.
    Agar koi number negative hai, to uska pehla signed digit negative hoga:
    jaise ki -123 ke signed digits hote hai -1, 2, aur 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    # kai sea
    ke = int(arr[0])
    if ke < 2:  # jay, hej
        return 0
    if ke < 1:  # toh, hay
        return 1
    if ke < 6:  # toh, hay, hi
        return ke - 1
    if ke < 9:  # zha, hay, hi, hia
        return 6 - ke

    # un niedhäm
    n = ke - 1

    # ke aur
    ke = 1 if n <= 3 else 0
    return ke
