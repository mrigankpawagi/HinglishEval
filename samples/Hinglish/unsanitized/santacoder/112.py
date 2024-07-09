
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
    s_list=list(s)
    s_list.reverse()
    result=[]
    for i in s_list:
        if i==c:
            pass
        else:
            result.append(i)
    if result==s:
        return False
    return True

