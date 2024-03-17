
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return str(n) == str(n)[::-1] and sum([int(i) for i in str(n) if int(i) % 2 == 0]) == n

##############
### TEST TEST ###
##############

# Test 1
# print is_even(10)
# print is_even(11)
# print is_even(2)

# Test 2
# print is_even(4)
# print is_even(6)
# print is_equal_to_sum_even(4)
# print is_equal_to_sum_even(6)

# Test 3
# print is_even(3) == False
# print is_equal_to_sum_even(2) == False
# print is_equal_to_sum_even(4) == False
