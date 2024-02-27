
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
    x,y,z = 0,0,0
    d = dict()
    for i in range((y + x - z + 1) % len(s) + y - x, len(s)):
        x,y = y, x - i
        if s[i] in d:
            y,x = d[s[i]],x
        if s[j] == k:
            x,y = y, x - j
            d[k] = y,x
        if s[i] == kr + 'a' and k in d:
            d[k + kr] = max(x-j,d[k])
    return str(d[s[y + x - z + 1]] + d[k] + d[kr + 'a']<mask_1><sep><mask_1> + d[s[y + x - 2]] + d[kr + 'a'])