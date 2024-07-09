def count_up_to(n):
    """
    Ek function implement karo jo ek non-negative integer leta hai aur return karta hai ek array jisme pehle n
    integers hote hai jo prime numbers hai aur n se kam hai.
    Jaise ki:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


def is_prime(n):
    """
    Ek function implement karo jo ek non-negative integer leta hai aur return karta hai True jaise ki n prime hai
    aur False jaise ki n prime nahi hai.
    Jaise ki:
    is_prime(2) => True
    is_prime(3) => True
    is_prime(4) => False
    is_prime(5) => True
    is_prime(6) => False
    is_prime(7) => True
    is_prime(8) => False
    is_prime(9) => False
    is_prime(10) => False
    is_prime(11) => True
    is_prime(12) => False
    is_prime(13) => True
    is_prime(14) => False
    is_prime(15) => False
    is_prime(16) => False
    is_prime(17) => True
    is_prime(18) => False
    is_prime(19) => True
    is_prime(20) => False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
