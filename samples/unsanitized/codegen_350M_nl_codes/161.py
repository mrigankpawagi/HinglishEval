
def solve(s):
    """
    Aapko ek string s di gayi hai.
    Agar s[i] ek letter hai, to uska case reverse karo lower se upper ya vise versa, 
    nahi to waise hi rakho jaisa hai.
    Agar string me koi letters nahi hai, to string ko reverse karo.
    Function ko resulted string return karni chahiye.
    Udaharan
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    print s

if __name__ == "__main__":

    s = input()
    solve(s)

Input (s):

1234
1326
1234
ab
ab
AB
c                                                            
123 
123
123
123
123
AB
d                                                         
123
123
123
123
AB
#a              
c      
bcd  
bab 
bab 
ABC
f      
fkz  
fkz 
fkz
fkz
ab 
d 
e 
e
... etc

Output

1234
1326
123
123
123
AB
d
d
e
e
AB
f
f
AB
f
f
f
AB
f
f
AB
f
f
AB
f
AB
