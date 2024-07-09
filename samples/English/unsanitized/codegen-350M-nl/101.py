
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Note 'words_string()' does the logic of splitting the strings
    print len(s)
    for i in range(len(s)):
        words = s[:i].split(',')
        for j, word in enumerate(words):
            if(word.lower()==' '):
                continue
            elif(word.lower()==" "):
                continue
            else:
                print(i, ",", j, end="\n")
    return words

