
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
    if n < 1:
        return (-1, -1)

    even = True

    while even:
        n += 1
        for i in range(1, n):
            if even:
                even = False
                yield [i, i]
            else:
                a, b = even_odd_palindrome(i)     # even yi, even fwa yhi, odd fwo yri
                a = -((a - 2) / 3)
                b = -((b - 2) / 3)
                yield (i, a)
                yield (i, b)

    try:
        i = 0
        y = (-3, 2)            # hai, in me, hain
        i = i + 1
        while (i < 3):
            c, d = even_odd_palindrome(i)    # ever i, ever ek i, even hain.

            i = (i + 1)         # 1,2,3,4
            j = len(y)          # 1,2,3,4
            i = j - 1
            j = i - 1

            x, y