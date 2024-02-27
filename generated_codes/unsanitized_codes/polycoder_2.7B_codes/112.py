
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
    s = str(s)
    c = str(c)
    if len(s) < 1:
        return ""
    elif len(c) == 1 and len(c)<len(s):
        k = s[0]
        h = s == c
    else:
        k = c
        h = c == c
        for i in reversed(range(1,len(s)+1)):
            r = s.replace(i,i+k,"")
            t = s.replace(i,i+h,"")
            if t==r:
                if len(s) < i:
