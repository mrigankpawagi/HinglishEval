
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
    s = ""
    # first check if the character in string is an ASCII code
    if s[:4] == 'a' or 'i' or 'o' or 'u' or 'v' or 'a' or 'b' or 'c' or 'd' or 'e' or 'f':
        s += "A"
    # if the character is a hexadecimal code, use the hexadecimal
    elif 0x20 <= s[0] and s[0] <= 0x7E:
        x = s.rjust(4, 'A')
        s += "\x{0x{3C}". format(x, 0x7E, x, 0x20, s[4:])
        # if we are on an odd number
        #    then we know in which character is the number
        #    we are looking for
        #    for example, in "hello"
        #    the first hexadecimal character must be "HELLO"
        # else, in the last line of the following code we use the string literal
        #    in the same order as shown above
        #    this will allow each hexadecional