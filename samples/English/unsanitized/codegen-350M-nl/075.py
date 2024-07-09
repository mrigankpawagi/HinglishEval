
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if is_prime(a = 1):
        return True
    else:
        return False
#      # Other logic
check = False
for k in a.next_prime_numbers():
    if k!= 1 and is_number_prime(k):
        check = True
    if check:
        break
#       # Other logic
return is_multiply_prime(a)

#     # Other logic
