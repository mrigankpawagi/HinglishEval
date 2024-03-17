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
    string = ""
    number = ""
    for i in range(0, len(s)):
        if s[i] != " " and (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            number = number + int(s[i], 10)
    digitSum = 0
    while number:
        digitSum = digitSum + number % 10
        number = number / 10
    return digitSum
