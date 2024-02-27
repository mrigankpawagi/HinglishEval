
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
    result = ""
    a = ""
    for i in s:
        if i == "A":
            a = "A"
        elif i == "B":
            a = "B"
        elif i == "C":
            a = "C"
        elif i == "-A":
            a = "a"
        elif i == "-B":
            a = "b"
        elif i == "e":
            a = "E"
        elif i == "^":
            a = "H"
        elif i == "f":
            a = "i"
        elif i == "H":
            a = "H"
        elif i == "o":
            a = "O"
        elif