
def digitSum(s):
    """
    Task
    Ek function likho jo ek string ko input ke roop mein leta hai aur sirf upper characters'
    ASCII codes ka sum return karta hai.

    Udaharan:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    x = 0
    for i in range(len(s)):
        if s[i].isupper():
            x += ord(s[i]) - 64
        else:
            x += ord(s[i]) - 96
    return x
print(digitSum("hELLooo"))

