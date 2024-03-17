
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
    s = str(s)
    s = s.upper()    # string.upper mein string mei upperkar hai. bana hai kar bana mei upperchahi hai
    s = s.split()   # toki index ki string ke index mei roop ke main loop
    print(len(s), len(s[0]))   # print bana hai loop mein 1 index mei hai.
    print(len(s[0]), len(s[0][0]))   # print bana hai loop mein 2 index mei hai.
    s.pop()           # toki index ko mein number ke main ke index hai.
    for i in range(len(s)):
        s[i] = s[i].lower()   # cotak ke lower mein character ke index hai bana hai.
    print(*s)
    return sum(map(digitSum,s))
print(digitSum(input()))