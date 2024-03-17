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
    i, k = 1, len(s)
    if j == k:  # if word starts at same index
        if a != b:
            result = "".join([a, b, a, b, a, b, a, b])
        else:
            result = s[:k] + s[k] + s[1:k]
            return result
    if s[i - 1] == "a":  # if word have one A
        for j in range(k + 1):
            result = result + a + s[j]
        i -= 1
        return s[:i] + result + s[k:]
    else:  # if word don't have "a"
        for j in range(k + 1):
            result = result + s[j]
        try:
            n = i - k - 1
        except ValueError:
            n = -1