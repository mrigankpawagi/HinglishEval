
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    startcount = int(len(string))
    for x in range(2, startcount+1):
        if startcount % x == 0:
           return False
    return True

def longest_substring(string):
    """Write a function that takes a string and returns the
    length of the longest substring within it.
    If there are two or more substrings of the same length,
    you may return either of them.
    Examples
    longest_substring('banana') == 5
    longest_substring('rabbits') == 6
    longest_substring('abcabcabcd') == 3
    longest_substring('bananaanananananananananana') == 28
    """
    if len(string) == 1:
        return 1
    counter = 0
    string = string.upper()
    a = 0
    b = 0
    while counter >= 0:
        for n in string[b:]:
            counter += 1
            if c in string:
                a = string.find(c)
        b = counter - a
    return b
