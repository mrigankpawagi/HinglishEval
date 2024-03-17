def reverse_delete(s, c):
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
    # Your code here
    s1 = s
    s2 = s
    for i in c:
        s1 = s1.replace(i, "")
        s2 = s2.replace(i, "")
    if s1 == s2[::-1]:
        return (s1, True)
    else:
        return (s1, False)
