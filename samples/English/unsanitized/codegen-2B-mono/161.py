
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    s = s.upper().replace(" ", "")
    if s == "":
        if s[0]!= s[len(s) - 1]:
            return s[len(s) - 1] + s[:len(s) - 1]
        return ""
    s = s.count('#')
    if s == 0:
        return ""
    else:
        result = ""
        for i in range(s):
            result += "#" + s[len(s) - i - 1]
        return result
