
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
    result = input.apply(int)
    kv = s + result[1:].upper()
    print ("Input: " + s)
    #print kv
    #decimal.decimalize
    return kv

input = input("Please enter the sequence of digits in which your user needs to be converted to ascii for: ")
s = digitSum("-")
print (input)

digitSum = digitSum[:]  

if digitSum[0] == ord("0"):
    for digit in digitSum[0:]:
        result = input.apply(int)
    print "Input: " + s       
    if digitSum[0]!= ord("0"):
        pass

print "Input: " + digitSum[0] + " ascii code"         
c = ord("0")
print c

if digitSum[1] == ord("1"):
    for digit in digitSum[1:]:
        print "Input: " + s       
        if digits in digitSum[1:]:
            print "1"
            pass
