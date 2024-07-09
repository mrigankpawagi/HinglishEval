
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    i = 0
    while i < 500:
        if string[i] == 'x':
            return False

        # Check that every element in string is an integer and if there is any,
        # start by removing all that are equal to 0
        while i < len(string) and string[i] <= 'x':
            string = string[:i] + string[i+1:]
        i += 1

    for j in range(3, len(string)):
        if string[j]!= 'x':
            continue
        else:
            break
    else:
        return False

    while j < 500:
        string = string[:j] + string[j+1:]
        j += 1

    for k in string:
        if k == 'x':
            return False
        else:
            i += 1
            continue
        # Check that every element in string is greater than 0
        if len(string) == 100:
            return False
    else:
        return True

