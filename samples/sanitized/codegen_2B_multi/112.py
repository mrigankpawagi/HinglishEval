
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
    temp = ""
    result = []
    index = -1
    for i in range(len(c)):
        if i:
            temp += c[:i]
        temp += s[i]
        result.append(temp)

    for i in range(len(c), len(s)):
        temp = ""
        index = -1
        for j in range(len(s) - 1, -1, -1):
            if j:
                temp += s[j]
            temp += c[: j + 1]
            index = temp.count(temp.lower())
            if index > 1:
                result.append(temp)
        temp = ""
        for j in range(len(s) - 1, -1, -1):
            temp += s[j]
            result[index + j].reverse()
            result[
                -math.ceil(math.log2(len(s) - (j + 1)))
                - (len(s) / 2)
                - 1 : -(len(s) - (j + 1))
            ] = (
                "".join(result),
                False,
            )  # reverse

    return result
