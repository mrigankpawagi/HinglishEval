
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
    # if len(s)==0:
    #     return 0
    # if (len(s) - 1) == 0:
    #     return 0
    s = s.upper()
    ans = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            ans += (ord(s[i])) - 48

    return ans
    # return(sum(ord(x)-48 for x in s))

print(digitSum(""))
print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))