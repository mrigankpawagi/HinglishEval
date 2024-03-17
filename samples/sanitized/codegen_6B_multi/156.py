
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
    if number < 1 or number > 1000:
        raise argparse.ArgumentTypeError("Invalid number")
    if number < 10:
        return str(number)
    smalles = 1
    for num in range(2, number + 1):
        if num < 10:
            smalles = num
        elif num < 20:
            smalles = 16
        elif num < 100:
            smalles = 19

        if (num - smalles) + 1 < number:
            break
    new_num = number
    for i in range(smalles, biges):
        new_num--
        if new_num % i == 0 and new_num!= 0:
            return int_to_mini_roman(number)

    # check for negative numbers
    if number > 9999:
        while number > 0:
            if number % 10 == 0 and number > 900:
                break
            else:
                number -= 1

        number += 1
    new_num = number
    for i in range(10, biges):
        if (number/i) % 10 == 0 and number - i >= 0:
            return int_to_mini_roman(new_num)
