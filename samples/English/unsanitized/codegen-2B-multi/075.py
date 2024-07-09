
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    def test_number(m3):
        """Given a number of the form m*3m with >= 1, test if the number is a prime
        and return the prime number m
        """
        def is_prime(prime):
            """
                Returns True if prime is a prime number, False otherwise.
                Is slow and slow but does not take too much time to run.
            """
            if prime < 2:
                return False  
            elif prime == 2:
                return True
            for i in range(2, int(ceil(prime/2))+1):
                if prime % i == 0:
                    return False
            return True
        prime = 3
        remainder_a = m3 % prime
        while remainder_a > 0:
            test_number(prime)
            prime += 1
            remainder_a = m3 % prime
        return prime

    test_number(a)

a = raw_input("Type a number greater than 100:")
result = is_multiply_prime(int(a))
if result:
    print "The number is a multiples of three prime numbers"
else:
    print "The number is not a multiples of three primes"
