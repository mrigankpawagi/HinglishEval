
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    result = []
    word = c.upper().split()
    char_values = word.split(" ")
    if char_values[0] in character_set_words:
        i,j = s.find(character_set_words[char_values[0]][0])
        if i is not True and i+1 < len(char_values):
            char_values[i+1] = char_values[i]
    else:
        char_values = ''
    if char_values in word:
        word[0] = '.'
    word = word[len(word)-1:]
    if len(word) == 1:
        result |= None
    if reverse_delete(s,char_values) in result:
        result = [s]
        word = [1] + word
        return result

