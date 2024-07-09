
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
    if n < 2:
        return (0, 0)

    even_cnt = 0
    odd_cnt = 0
    for c in range(1, n):

        # if both are an even number
        if n % c == 0 and n % (n+1) == 0:
            even_cnt += 1
            odd_cnt += 1

        # if only one is an even number
        elif n % c == 0:
            odd_cnt += 1

        # if only one is an odd number
        elif n % (n+1) == 0:
            even_cnt += 1

        # if neither one is an even number nor an odd number
        else:
            continue

    return (even_cnt, odd_cnt)


if __name__ == '__main__':
    n = 22
    print(even_odd_palindrome(n))
