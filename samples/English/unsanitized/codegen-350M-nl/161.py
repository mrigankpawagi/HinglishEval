
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
    if not s:
        return None
    word = s
    res = ''
    for i,word in enumerate(word.split()):
        if len(word) > 1:
            res = " " * 2 + res
    return res
    
