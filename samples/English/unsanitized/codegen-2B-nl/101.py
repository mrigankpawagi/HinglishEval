
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words_array = []
    for word in s.split(', '):
        if startswith(word, '"') or startswith(word, '"n'):
            words_array.append(word.strip('"').lower())
        else:
            words_array.append(word.strip())
    return words_array

