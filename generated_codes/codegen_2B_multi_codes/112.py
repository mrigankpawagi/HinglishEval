
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
    s_rev = []
    i=0
    a=0
    b=0
    c_rev=[]
    c=[char for char in c]
    while  b!= len(s) - 1: 
        if s[b] == c[a]:
            b=b+1
            a=a+1
            c_rev.append(s[b-1])
        else:
            s_rev.append(s[b-1])
            if c[i-1] == s[b]:
                i=i+1
                c_rev.append(s[b-1])
            else:
                c_rev.append(s[b])
            b=b+1
            a=a+1
        print(i,",",len(s)," ",b," ",a)
    s_rev.append(s[a-1])
    return s_rev, not palindrome(s_rev)

myInput="a2ca2cad22ca2cd1ca2d"
print(palindrome(myInput))
