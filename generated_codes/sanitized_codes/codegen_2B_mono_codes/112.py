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
    p = len(s)
    q = len(c)
    s_r = s[p : len(s)]
    c_r = c[q : len(c)]
    k = s_r + c_r
    if len(k) % 2 == 0:
        return (k[len(k) // 2 - 1 : len(k) // 2 + 1], False)
    else:
        return (k[len(k) // 2], False)