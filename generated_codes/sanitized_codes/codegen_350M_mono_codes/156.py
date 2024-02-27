def int_to_mini_roman(number):
    """
    Diye gaye positive integer ko uska roman numeral equivalent ke roop mein string ke roop mein prapt karo,
    aur ise lowercase mein return karo.
    Restrictions: 1 <= num <= 1000
    Udaharan:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    int_dict = {1: "I", 5: "v", 10: "l", 50: "d", 100: "cc"}
    res = []
    for i in range(len(number)):
        v = int(number[i])
        v1 = sum(x != 0 for x in int_dict.values())
        res.append(
            int_dict[v + v1 * len(int_dict)] if int_dict.get(v + v1) != None else "I"
        )
    return "".join(res)