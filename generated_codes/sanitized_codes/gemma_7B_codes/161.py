
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
    # Your code here
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
    if s[0].isalpha():
        s = s[::-1]
    return "".join(s)
