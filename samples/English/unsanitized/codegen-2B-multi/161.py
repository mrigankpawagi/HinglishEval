
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
    n = len(s)
    dp = [-1]*(n*2-1)
    ans = []
    
    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            ans.append("".join((chr(ord(c)+256-32), chr(ord(c)))));
        else:
            ans.append(s[i])
    
    dp[0] = ans[0]
    for x in range(1, n*2-1):
        dp[x] = max(dp[x-1], dp[x-2] + (x&1 if x&1 else -1))
    return dp[n*2-1]
