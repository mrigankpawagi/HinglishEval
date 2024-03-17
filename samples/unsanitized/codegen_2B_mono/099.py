
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
    return -1 if value.upper() == "NAN" else math.trunc(float(value)) if abs(float(value) - int(value)) else int(
        value)


# Input data:
print("Example- 1")
print(closest_integer("10"))  # Should return 10
print(closest_integer("3.5"))  # Should return 3
print(closest_integer("10.5"))  # Should return 10
print(closest_integer("3.555"))  # Should return 3
print(closest_integer("-6.95"))  # Should return -7
print()

print("Example- 2")
print(closest_integer("145635647987"))  # Should return 14
print("Example- 3")
print(closest_integer("1457"))  # Should return 14
print("Example- 4")
print(closest_integer("-14.554"))  # Should return -14
print("Example- 5")
print(closest_integer("55.5"))  # Should return 55
print("Example- 6")
print(closest_integer("-55.5"))  # Should return -