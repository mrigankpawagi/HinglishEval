
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
    if not isinstance(value,str):
        raise TypeError("value must be string type")

    try:
        d = int(value)
        if not 1 <= d <= 65536:
            raise ValueError("value must be integer")
        d = d % 1000
        d = d // 1000

        d -= 1
        if -10000 < d < 10000:
            result = d * 10 + 1
        elif 10000 <= d <= 65999:
            result = d
        else:
            if d < 0:
                if d * -1 < 0:
  