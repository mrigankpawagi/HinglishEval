
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
    i, n = 0, len(s)
    flag='#'
    l = []

    while i < n:
        if s[i].isalpha():
            if s[i] == flag:
                l.append(flag.upper())
            else:
                l.append(flag.lower())
            i+=1
        else:
            j = 2*i+1
            li = l[j:j]
            li.append(s[i])
            l.extend(li)
            l.pop()
            flag = s[j]
            i+=1
    return l[0].upper()+l[1:] if len(l) else l[0]

print(solve("ab"))
print(solve("#a@C"))
