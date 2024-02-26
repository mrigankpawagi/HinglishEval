
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
    s1 = s[0].upper()
    if len(s) < 2:
        return 0
    return sum([ord(a) + ord(b) for a in s if ord(a.upper()) >= ord('A') and ord(a.upper()) <= ord('Z')
            for b in s if ord(b.upper()) >= ord('A') and ord(b.upper()) <= ord('Z')])

