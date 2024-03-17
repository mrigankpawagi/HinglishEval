
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
    solver = re.sub('[A-Za-z]+', lambda s: "".join(s[::-1].lower()+s[::-1].upper()), s, 1)
    print solver
    return solver


n = raw_input("Enter no of strings :")
while n!= '0':
    if n == '0': break
    n -= 5
    s = ''.join(raw_input("Enter string " + str(n + 1) + "... :").upper())
    s = solver(s)
    print s
    s = ''.join(s)
    sender = raw_input("Enter string " + str(n + 1) + " again :")
    #print sender
    sender = solver(sender)
    print sender


    

