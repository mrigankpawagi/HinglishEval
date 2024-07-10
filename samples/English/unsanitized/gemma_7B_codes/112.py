
def reverse_delete(s,c):
    """
    Task
    Humare paas do strings s aur c di gayi hain, aapko s mein se un sabhi characters ko delete karna hai jo c ke kisi bhi character ke barabar hain
    phir check karo ki resultant string palindrome hai ya nahi.
    Ek string ko palindrome tabhi kaha jata hai jab woh backward aur forward dono taraf se same padhti ho.
    Aapko ek tuple return karna hai jisme resultant string aur True/False check ke liye hoga.
    Udaharan
    Agar s = "abcde", c = "ae", toh result ('bcd',False) hona chahiye
    Agar s = "abcdef", c = "b"  toh result ('acdef',False) hona chahiye
    Agar s = "abcdedcba", c = "ab", toh result ('cdedc',True) hona chahiye
    """
    if s == "":
        return False
    elif s[0] in c:
        return reverse_delete(s[1:],c)
    elif s != c:
        return True
    elif s == c:
        return reverse_delete(s[1:],c)


class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    def reverse_delete(self, S, C):
        # write your code here
        if len(S) == 0:
            return False
        if S[0] in C:
            return self.reverse_delete(S[1:],C)
        elif S != C:
            return True
        else:
            return self.reverse_delete(S[1:],C)


s = "abcde"
c = "ae"
print(reverse_delete(s,c))
