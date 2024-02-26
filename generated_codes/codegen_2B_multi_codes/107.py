
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
    # Step1: Remove n from range (1, n+1). Find k.

    k = n/2

    # Step2: Return pair (p[0], p[1]), where:
        # p[0] - number of even integer palindrmons.
        # p[1] - number of odd integer palindrmons.

    p = [0, 0]
    p[1], p[0] = even_odd_palindrome(k)
    p[1], p[0] = odd_even_palindrome(p[1])

    return p

#############################################################################################################
# Problem 3: Odd even Integer
#############################################################################################################

# [tag]: [note]:
