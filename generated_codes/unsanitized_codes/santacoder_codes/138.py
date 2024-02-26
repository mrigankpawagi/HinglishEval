
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_of_even = 0
    for x in range(1, n + 1):
        if x % 2 == 0:
            sum_of_even += x
    if sum_of_even == n:
        print(f'n is a sum of even number: {n} = {sum_of_even}')
        return True
    else:
        print(f'n is not a sum of even number: {n} = {sum_of_even}')
        return False

