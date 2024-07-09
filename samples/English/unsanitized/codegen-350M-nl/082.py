
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    cmp_string = "Hello"
    m_primelength = sum(len(c) for c in string.split())
    return prime_length(cmp_string) == prime_length(string)

A:

You have an array of ints:
val = '0123'

I'm giving the compiler a chance to optimize that, but for the purposes of this experiment I'll assume that there's nothing that uses C or C++ that takes any more than O(n^2).
So, you want:
