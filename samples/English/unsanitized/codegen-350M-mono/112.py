
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
    def get_len(s):
        length = 0
        for char in s:
            length += ord(char) - ord('a')
        return length
    def palindrome(s,c,s0,c0,count):
        if len(s)<=2:
            if count == get_len(s):return [(s,True)]
        else:
            if c == c0:
                if count+1 < get_len(s):
                    if not remove3s(s,count):
                        #return [s,get_len(s)<get_len(s0)]
                        return
                    s2=get_reverse_str(s)
                    if palindrome(s2,c,s0,s0,count+1):
                        return [s,check_reverse(s2,c,s0,s0,count+1)]
                if count == get_len(s):
                    s=s+"0"
                    return
            else:
                if count+3<get_len(s):
                    if not remove2s(s,count,s0):
                        return
                    s2=get_reverse_str(s)
                    if not palindrome(s2,c,s0,s0,count+2):
                        return
                    s2=get_reverse_str_2(s)
                    if palindrome(s2,c,s0,s0,count+