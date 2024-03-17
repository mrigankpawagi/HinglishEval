
def prime_length(string):
    """
    Ek function likho jo ek string leta hai aur return karta hai True agar string 
    ki length ek prime number hai ya False otherwise
    Udaharan
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) < 2 or string[0 - 1]!= '#':
        return True
    if string[0] is not string[len(string) - 1]:
        return False
    for i in range(2, int(string) + 1):
        if string[i - 1:i]!= string[0:i - 1]:  
            return True
        

for index in range(6, 9):
    for test in prime_length(str(index) +'' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'):
        print test
