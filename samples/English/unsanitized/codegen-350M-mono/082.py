
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    for index, char in enumerate(string.lower()):
        if 'j' not in string[index:index + 5]:
            return False
    return True

# TODO: Add the file-object as a way to read data from bytes and send back to bytes
# the file has to be a csv data file, it can be a json file too be the data.
# This one is just not so useful for testing purposes but it will take some time
