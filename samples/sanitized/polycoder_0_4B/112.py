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
    s = s.strip()
    if s not in c:
        return
    if (
        s[0] in "ae"
        and s[1] in "ae"
        and s[2] in "ae"
        and c[0] not in "a"
        and c[1] not in "a"
        and c[2] not in "a"
        and c[3] not in "a"
        and c[4] not in "a"
        and c[5] not in "a"
        and c[6] not in "a"
        and c[7] not in "a"
        and c[8] not in "a"
        and c[9] not in "a"
        and c[10] not in "a"
        and c[11] not in "a"
        and c[12] not in "a"
        and c[13] not in "a"
        and c[14] not in "a"
        and c[15] not in "a"
    ):
        return
    c
