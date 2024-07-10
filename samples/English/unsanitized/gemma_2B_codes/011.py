from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_list = []
    # print(a)
    # print(b)
    for i in range(0,len(a)):
        # print(a[i])
        xor_list.append(ord(a[i]) ^ ord(b[i]))    
    return ''.join([ chr(x) for x in xor_list ]).lower()
    # return ''.join(chr(24 | ord(a[i]) ^ ord(b[i])) for i in range(0,len(a)))


def is_prime(number: int) -> bool:
    """ Input is the number we want to determine if it’s prime or not.
    Check if the number is a multiple of any number from 2 to the square root of the number.
    If it isn’t a multiple of any number from 2 to root, it’s considered a prime.
    """
    if number % 2 == 0:
        return False
    for i in range(1, int(number ** 0.5)):
        if number % i == 0 and number // i != i:
            return False
        if i == number // i and number != i:
            return False
    return True
    
def prime_numbers(limit: int) -> List[int]:
    prime_numbers = set()
    
    for i in range(3, limit, 2):
        # print('*'*30)
        # print(i)
        if is_prime(i):
            prime_numbers.add(i)

    return list(prime_numbers)


# prime_numbers_10 = prime_numbers(10)
# print(prime_numbers_10)
