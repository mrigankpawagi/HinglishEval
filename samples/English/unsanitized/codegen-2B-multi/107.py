
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    def even_odd_palindrome(num):
        if num == 0:
            return ()
        elif num <= 1:
            yield (1, 1)
            return
        elif num % 2 == 0:
            yield (1, num/2) + even_odd_palindrome(num/2)
            return
        else:
            yield (1, num) + even_odd_palindrome(num-1)
    even_odd_palindromes = even_odd_palindrome(n)
    return tuple(even_odd_palindromes)


my_even_odd_palindrome = even_odd_palindrome(12)
print(my_even_odd_palindrome)
