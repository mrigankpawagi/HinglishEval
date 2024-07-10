
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
    mini_roman_dict = {1:'i',5:'v',10:'x',50:'l',100:'c',500:'d',1000:'m'}
    str_num = min_num1 = str()
    final_value = num =  number 
    str_num += mini_roman_dict[final_value%500]
    final_value = (final_value-final_value%500)/500
    str_num += mini_roman_dict[final_value%100]
    final_value = (final_value-final_value%100)/100
    str_num += mini_roman_dict[final_value]
    return str_num 
    


"""

Question:
    Problem Link: https://www.spoj.com/problems/INT2MR/

"""
