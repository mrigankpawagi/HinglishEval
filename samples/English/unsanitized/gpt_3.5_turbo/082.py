def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)
    if length < 2:
        return False
    for i in range(2, int(length/2)+1):
        if length % i == 0:
            return False
    return True