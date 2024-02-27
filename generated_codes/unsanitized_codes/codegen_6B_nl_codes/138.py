
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a = [1,2,3,4]
    for i in range(10):
        nums = [i] + a
        if is_sum_of_even_ints_in(nums, n):
            return True
    return False

print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))

A:

There is a problem with your code:
In the case of the 8th number you never test if the sum is equal to 8. You check if the nth number is 4 - you are missing an else.

To get more meaningful feedback, put print statements right before and after the try:
