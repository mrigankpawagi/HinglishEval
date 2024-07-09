
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
    r = (c if c==cend else c+2)
    if c == r: #the char in c is the same, we find if the two lengths of c and r are equal
        return (r,True),(r-c,False)
    if c==s: #check if c is same string
        return (s,False)
    start = c
    end = start
    while end < len(s):
        b = ord(s[end])
        eb = ord(c)
        if b == eb: #check if 'b' is equal with 'c', if not, return None
            return None
        if b > eb:
            end += 1
        else:
            end = c
    return None

s = """8x3a"""
res = reverse_delete(s,['b','c','a'])
assert res[0] == (b,False)
assert res[1] == (b-c,True)

s = """8x2a3x4x3"""
res = reverse_delete(s,['a','c','b'])
assert res[0] == (b,True)
assert res[1] == (b-c,False)

#
# Test
#
