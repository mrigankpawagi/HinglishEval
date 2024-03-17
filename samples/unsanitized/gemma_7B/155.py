
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


# 2
def count_digits(num):
    """
    Ek integer diya gaya hai. Ek integer return karo jo digits ki sankhya ko darshata hai.

     Udaharan:
        count_digits(12345) ==> 5
    """
    return len(str(num))


# 3
def count_digits_2(num):
    """
    Ek integer diya gaya hai. Ek integer return karo jo digits ki sankhya ko darshata hai.

     Udaharan:
        count_digits_2(12345) ==> 5
    """
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


# 4
def count_digits_3(num):
    """
    Ek integer diya gaya hai. Ek integer return karo jo digits ki sankhya ko darshata hai.

     Udaharan:
        count_digits_3(12345) ==> 5
    """
    return len(str(num))


# 5
def count_digits_4(num):
    """
    Ek integer diya gaya hai. Ek integer return karo jo digits ki sankhya ko darshata hai.

     Udaharan:
        count_digits_4(12345) ==> 5
    """
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


# 6
def count_digits_5(num):
    """
    Ek integer diya gaya hai. Ek integer return karo jo digits ki sankhya ko darshata hai.

     Udaharan:
        count_digits_5(12345) ==> 5
    """
    return len(str(num))


# 7
def count_digits_6(num):
    """
    Ek integer diya gaya hai. Ek integer return karo jo digits ki sank