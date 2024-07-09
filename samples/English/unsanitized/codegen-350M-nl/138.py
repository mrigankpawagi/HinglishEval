
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    try:
        return sum(is_equivalent_even(k,j)) == sum(is_equivalent_even(n[4],n[5],n[6]))
    except (TypeError, NameError):
        # No sum is equal to 4x4.
        pass

# Function to get sum even number
