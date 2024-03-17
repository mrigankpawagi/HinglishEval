
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

    sum = 0
    for x in s:
       sum += int(x)

    return sum


