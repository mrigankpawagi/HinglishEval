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

    s = ""
    # 0 <= number < 1000
    for i in range(1, 1000):
        # num > number?
        result = int(number / i)
        if result < 1:
            break
        s = _int_to_roman(result)
        if i < 10:
            break
    # num > number?
    return s
