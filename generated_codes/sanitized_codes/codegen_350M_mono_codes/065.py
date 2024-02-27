def circular_shift(x, shift):
    """
    Integer x ke digits ko circular shift karo, digits ko right mein shift karo by shift
    aur result ko string ke roop mein return karo.
    Agar shift > digits ki number ho, toh reversed digits return karo.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = "0123456789"
    list = []
    index = 0
    num = digits[index]
    list.append(num)
    shift = int("".join([num[i] for i in range(shift - 1)]))
    while num < digits[index]:
        if num % 2 == 0:
            list.append(num)
            index = index + 1
            num = digits[index]
        else:
            list.append(num)
            index = index + 1
            num = digits[index]
    return "".join(list[1 : (len(list) - 1)]) + "".join(list[0 : (len(list) - 1)])