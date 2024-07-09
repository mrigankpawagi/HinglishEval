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
    """  # O( n )
    def check(n):  # a. function defined
        for i in range(1, n // 2 + 1):
            if int(n / 2**i) % 4 == int(n / 2 ** (-i)):
                return (i, n - i * 2 ** (-i))
        print("No even palindrom")
        return 0  # b. function return
    for p in check(n):  # c. loop defined
        if int(p * 2 % 11) == int(n % 11**2 - p):
            if str(p) == str(p)[::-1]:
                return (p, p * 2 % 11)
    print("No even palindrom")
    return 0