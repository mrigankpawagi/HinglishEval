
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # you can use the built-in sum function here instead.
    # You are given a number n.
    # Your task is to return "true" if there is no number n that
    # adds up to the sum of even numbers between 1 and 9, inclusive.
    # Otherwise, return "False".
    # return
    return len(list(filter(is_sum_even, itertools.range(1,10)))) == 0


print(is_equal_to_sum_even(1))
print(is_equal_to_sum_even(2))
print(is_equal_to_sum_even(3))
print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(8)) # This is what you expected to return from your method.