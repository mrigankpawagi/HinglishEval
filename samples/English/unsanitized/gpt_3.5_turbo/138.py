def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    count = 0
    for i in range(2, n+1, 2):
        for j in range(2, n+1, 2):
            for k in range(2, n+1, 2):
                for l in range(2, n+1, 2):
                    if i + j + k + l == n:
                        count += 1
    if count == 1:
        return True
    else:
        return False