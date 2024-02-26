
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
    s = str(s)
    s = "_".join([chr(i) for i in range(ord('A')+1, ord('Z')+1)])
    return sum(d for d, _ in map(ord, s))

How to achieve this using Python's string API

A:

s[0 :: 4] is one way
s[1 :: 4] returns an empty string

>>> s = s[0 :: 4] + s[1 :: 4]
>>> s == ''
False
>>> s_ = s[1 :: 4]
>>> s_ == ''
True

