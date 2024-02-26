
def prime_length(string):
    """
    Ek function likho jo ek string leta hai aur return karta hai True agar string 
    ki length ek prime number hai ya False otherwise
    Udaharan
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    for i in range(5):
        print(ekelu_prime(string)[i], prime_length(string)[i])

A:

use is_prime_number.
>>> import is_prime_number

>>> is_prime_number(elems)
True

>>> is_prime_number
True

>>> is_prime_number(elems)
True

It also works for strings, just use as many as you need.
>>> list(is_prime_number(list('abc'))) # => true
True

