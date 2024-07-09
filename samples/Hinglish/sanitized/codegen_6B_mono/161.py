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
    result = s[::-1]
    for i in range(len(s)):
        if not s[i].isalpha():
            continue
        if s[i].isupper():
            result = result.replace(s[i], s[i].lower())
        else:
            result = result.replace(s[i], s[i].upper())
    return result