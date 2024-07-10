
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    result = 0
    temp = ''
    # add only the letters
    for r in s:
        if r >= 'a' and r <= 'z':
            result+=ord(r)-64
    # if it's just one letter then we still have to convert it to an integer
    if len(s) == 1:
        result-=s[0].index(s[0]) # 97-64 = 33
    print("result: " + str(result))
    return result

print(digitSum(""), 0)
print(digitSum("abAB"), 131)
print(digitSum("abcCd"), 67)
print(digitSum("helloE"), 69)
print(digitSum("woArBld"), 131)
print(digitSum("aAaaaXa"), 153)
