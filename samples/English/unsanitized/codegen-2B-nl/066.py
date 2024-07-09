
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
    s = s.upper()
    n = len(s)
    sum_ = 0
    for i in range(n):
        sum_ += ord(s[i] + 'a')**2
    return sum_
print("Enter a string:")
string = input()
print(digitSum(string))

