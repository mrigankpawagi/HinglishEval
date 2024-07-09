
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

    return (min(i:i for i in range(len(range(1,n))+1)), max(j:j for j in range(len(range(1,n))+1)))

print(even_odd_palindrome(1), even_odd_palindrome(2), even_odd_palindrome(10))

The output is as follows:

(1, 2) (4, 6) (11, 11)

The time complexity of this approach is still a mystery to me. Can anyone tell me how many times will be the recursion will go, and the running time?

A:

The recursive calls do not happen until the number is small enough, since the recursive calls will terminate early if the numbers they are asked to calculate are bigger than a reasonable maximum limit. As such we don’t have a limit, but we still will probably see linear time