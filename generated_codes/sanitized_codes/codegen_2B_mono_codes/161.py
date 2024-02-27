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
    # print("Case 1 :",s)
    arr = []
    str_list = list(s)
    for i in str_list:
        (
            arr.append(chr(ord(i.lower()) + 32))
            if i.islower()
            else arr.append(chr(ord(i) + 32))
        )
    # print(arr)
    # res_str = "".join(arr)
    res_str = "".join(arr)
    # print("Case 2:", res_str)
    return res_str