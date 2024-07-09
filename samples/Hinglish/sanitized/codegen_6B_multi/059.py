def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 1. If n < 2 then return 1.
    if n < 2:
        return 1
    # 2. If n is integer.
    # 3. Else return 2.
    if not n % 1 == 0:
        return 2
    # 4. for i in range(3, int(n**0.5) // 2).
    # 5. n-i >= 1.
    # 6. for j in range(i, n//i + 1).
    # 7. n-i-j >= 1.
    # 8. j is prime.
    # for i in range(3, int(n**0.5)//2):
    #     if (n - i) > 0 and n-(i)%1==0 and n-i>=1 and n-i-j>=1 and j%1==1:#j=prime.
    #         return i