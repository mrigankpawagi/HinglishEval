
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
    if s == "":
        return 0
    try:
        res = int(s.upper())
    except:
        return -1

    for ch in s:
        res += int(ch.upper())
    return res


# This function removes all the extra whitespaces in a string,
# for instance, a,     b,c,and     d,
# results in the output a,b,c,d
