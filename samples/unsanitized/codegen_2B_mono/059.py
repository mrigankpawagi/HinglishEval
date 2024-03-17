

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i >= 1:
        if n % i == 0:
            return i
        i = i + 1

# print(largest_prime_factor(13195))
# print(largest_prime_factor(2048))

# n = int(input('Enter the number: '))
# if n <= 0:
#     print('Invalid input')
# elif not n % 2 and not n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17:
#     print('This number is a armstrong number')
# else:
#     if n % 2 == 0:
#         n = n/2
#     if n % 3 == 0:
#         n = n/3
#     if n % 5 == 0:
#         n = n/5
#     if n % 7 == 0:
#         n = n/7
#     if n % 11 == 0:
#         n = n/11
#     if n % 13 == 0:
#         n = n/13
#     if n % 17 == 0:
#         n = n/17
#     if n!= 1:
#         print('this number is a armstrong number')
#     else:
#         print('prime')

# n = int(input('Enter n value: '))
# i = 2
# flag = 0
# while i < n :
#     factors = 0


# if n % 2 == 0 :
#     factors += 1
#     if n % 3 == 0:
#         factors += 1
#     if n % 5 == 0:
#         factors += 1
#     if n % 7 == 0:
#         factors += 1
#     if n % 11 == 0:
#         factors += 1
#     if n % 13 ==