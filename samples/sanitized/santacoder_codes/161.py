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
    x = "12345321"
    y = x.lower()
    z = x[::-1]
    if s[0].lower() == s[len(s) - 1].lower():
        return s.lower()
    else:
        result = s[0].lower()
        for i in range(len(s) - 1):
            if s[i].isupper():
                y = s[i] + y
            else:
                y = y + s[i]
        z = z + y
        for i in range(len(z) - len(s) - 1):
            if z[i].isupper():
                y = z[i] + y
            else:
                y = y + z[i]
        return z
    return 0
