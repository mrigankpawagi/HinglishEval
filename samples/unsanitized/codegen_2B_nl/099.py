
def closest_integer(value):
    """
    Ek function banaiye jo ek value (string) leta hai jo ek number represent karta hai
    aur uska sabse close integer return karta hai. Agar number do integers ke beech 
    samanantar hai, toh use zero se door round karo.

    Udaharan
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Dhyan Dijiye:
    Zero se door round karne ka matlab hai ki agar diya gaya number do integers ke beech 
    samanantar hai, toh aapko woh integer return karna chahiye jo zero se sabse door hai. 
    Jaise ki closest_integer("14.5") ko 15 return karna chahiye aur closest_integer("-14.5") 
    ko -15 return karna chahiye.
    """
    if value == 0: return 0  # 0 = min value 

    diff_max = Math.floor(Math.abs(value))
    diff_min = Math.abs(diff_max); 
    return diff_min;  # return diff_max if it's not integer otherwise return diff_max


# 
# ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####   ####