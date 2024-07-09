
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
    if(len(s)==len(c)):
        for i in range(len(s)):
            if(s[i]==c[i] and (s[i-1]!=c[i-1])):
                s=s[:i-1]
                return reverse_delete(s,c[i])
        for i in range(len(s)):
            if(s[i]==c[i]):
                s=s[:i]
        return s
    else:
        return False

print (reverse_delete("xyxxy","x"))
print (reverse_delete("ccbccdb","ab"))
print (reverse_delete("cdecfdea", "bcba"))
print (reverse_delete("dafegh", "fghij"))
print (reverse_delete("abcde", "def" ))
print (reverse_delete("A","A"))
print (reverse_delete("b",2))
# A = [["b","ab","c","dbd","e","f","gh","ij"],["a