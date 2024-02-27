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
    if not s:
        res = ""
        return res
    i = len(s) - 2
    while i > 0:
        sord = s[i]
        if sord == "A":
            sord = "A"  # upper case.
            i -= 1
        elif sord == "c":
            sord = "A"  # lower case.
            i -= 3
        else:
            sord = sord  # letter
        sord = sord.lower()
        if sord == "k":
            sord = sord.upper()
        else:
            sord = sord.lower()
        sord = sord.replace(" ", "")
        sord = sord.replace("-", "")
        sord = sord.replace("+", "")
        if sord in ("a", "b"):
            sordc = sordc.zfill(3)
        else:
            sordc = sordc.zfill(2)
        sordc = sordc.upper()
        s = s.upper()
        if sord == "x":
            sord = "X"  # x.
            i -= 1
        elif sord == "q":
            sord = "Q"  # c.
            i -= 2
        elif sord == "a":
            sord = "A"  # A.