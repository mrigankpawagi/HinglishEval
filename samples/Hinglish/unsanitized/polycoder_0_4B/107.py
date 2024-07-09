
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
    ans = [1] * 10
    ret1, ret2 = [], []
    for i in range(n):
        ret1.append(1)
        ret2.append(2)
    # 2, 3
    ret3 = ret1 + ret2
    ret4 = [2] * 12

    for j in range(4):
        for k in 0:
            ret4[k] += ret3[j]
    return ret4

