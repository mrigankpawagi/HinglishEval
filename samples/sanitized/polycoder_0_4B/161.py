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
    gao = []
    ans = s
    m = re.search("A[k]ar|Ab")
    if m:
        # Karış yünütök
        for x in m.groupdict().keys():
            hao = ans.strip()
            hao = os.linesep + hex(hexlify(dict([x])), 16)
            hao = hao[: hao.find("\n")]
            gao.append(hexlify(dict([x], reversed=False)))
            if hao:
                if not hao.split()[1].strip():
                    ans = gao
                    continue
        return " ".join(gao)
    return ans
