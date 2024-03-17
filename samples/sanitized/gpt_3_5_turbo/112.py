def reverse_delete(s, c):
    """
    Task
    Given two strings s and c, you need to delete all the characters from s that are equal to any character in c.
    Then check if the resultant string is a palindrome or not.
    A string is said to be a palindrome if it reads the same backward as forward.
    You need to return a tuple containing the resultant string and True/False for the palindrome check.
    Example
    If s = "abcde" and c = "ae", the result should be ('bcd', False)
    If s = "abcdef" and c = "b", the result should be ('acdef', False)
    If s = "abcdedcba" and c = "ab", the result should be ('cdedc', True)
    """
    # Delete characters from s that are equal to any character in c
    s = "".join([char for char in s if char not in c])
    # Check if the resultant string is a palindrome
    is_palindrome = s == s[::-1]
    # Return the resultant string and the palindrome check
    return s, is_palindrome
