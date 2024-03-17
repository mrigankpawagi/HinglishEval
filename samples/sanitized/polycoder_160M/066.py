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
    i = 0
    while i < len(s) and s[i] not in Karta:
        i = i + 4
    # print i, I, Karta
    for i in range(0, Karta.digitSum(s)):
        if s[i] == "":  # Ek
            return i
    return i
