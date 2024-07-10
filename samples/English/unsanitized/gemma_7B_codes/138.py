
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    for i in range(2, int(n/2) + 1):
        if n - i - 2 != sum(range(2, i)) and n - i - 2 != sum([i+2]):
            return False
        return True

print(is_equal_to_sum_even(8))
