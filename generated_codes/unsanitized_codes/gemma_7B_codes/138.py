
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n % 4 == 0


def is_equal_to_sum_odd(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive odd numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == True
    is_equal_to_sum_odd(8) == False
    """
    return n % 4 == 2


def is_equal_to_sum_even_odd(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 2 positive even numbers aur 2 positive odd numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even_odd(4) == True
    is_equal_to_sum_even_odd(6) == False
    is_equal_to_sum_even_odd(8) == False
    """
    return n % 4 == 0


def is_equal_to_sum_odd_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 2 positive odd numbers aur 2 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_odd_even(4) == False
    is_equal_to_sum_odd_even(6) == True
    is_equal_to_sum_odd_even(8) == False
    """
    return n % 4 == 2


def is_equal_to_sum_even_odd_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 1 positive even number aur 3 positive odd numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even_odd_even(4) == False
    is_equal_to_sum_even_odd_even(6) == False
    is_equal_to_sum_even_odd_even(8) == True
    """
    return n % 4 == 2


def is_equal_to_sum_odd_even_odd(n):
    """
    Evaluate karo ki diya