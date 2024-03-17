
def even_odd_palindrome(n):
    """
    Ek positive integer n diya gaya hai, return karo ek tuple jisme even aur odd integer palindromes ki sankhya ho jo range(1, n) ke andar aate hain, inclusive.

    Udaharan 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome hain 1, 2, 3. Inme se ek even hai, aur do odd hain.

    Udaharan 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome hain 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. Inme se chaar even hain, aur 6 odd hain.

    Dhyan de:
        1. 1 <= n <= 10^3
        2. returned tuple me even aur odd integer palindromes ki sankhya kramashah hoti hai.
    """

    # Solution 1
    # Time O(n):
    # Space O(1):

    # Solution 2
    # Approach 1:
    # 3 variables.
    #   n % 2 == 0 => is true.
    #   ((n // 2) - 1) % 2 == 0 => is true.
    #   We check if n is Even or odd. If n is even (n mod 2 == 0) we are going to use our variable even and if odd is (n - (n mod 2)) we are going to use our variable odd.

    # Approach 2:
    # 1 variable.
    #   Inme se kare (n < 3)
    #   inme se aur (n = 1, n = 2, 3, n = 10, n = 11).
    #   inme se odd (n = 6, n = 7, n = 8, n = 9, n = 11).

    # Approach 3:
    # 1 variable.
    #   Inme se kare (n == 1).
    #   Approach 1.