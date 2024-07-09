
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    num = 0
    a_2 = a // 1000
    a_100 = a_2 // 100
    a_500 = a_2 // 500
    a_1000 = a_2 // 1000

    if a > 1000:
        num += 3*a_2
    if a > 100:
        a_100 += a_2

    if a > 500:
        num += 2*a_2
    if a > 1000:
        a_500 += a_2
    if a > 100:
        a_1000 += a_2
    
    a_1 = num
    
    if a_2!= 0:
        if a_2!= a_100:
            return False
        
    if a_100 == 0:
        num -= 1000
        return num == 1
    if a_500 == 0:
        num -= 200
        return num == 2
    if a_1000 == 0:
        num -= 300
        return num == 3


if __name__ == '__main__':
    # is_multiply_prime(300) or is_multiply_prime(300) or is_multiply_prime(200)
    print("Passed." if is_multiply_prime(300) and is_multiply_prime(200) else "Failed!" )





