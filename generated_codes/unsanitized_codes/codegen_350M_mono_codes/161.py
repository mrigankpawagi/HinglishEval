
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
    s = s.rstrip('.').upper()
    s = s.replace('?', '*-') # jika string juga komple eal, dapatkan ke kanan ke dicom
    s = s.replace('-', '+-')
    return s.rstrip('.').upper() # to string koi letters hai.

if __name__ == '__main__':
    print(solve('1234'))    
    #print(solve("a@C"))
    #print(solve("#a@C"))
    print(check_balanced('3-6'))
    #print(check_balanced('.8+'))
    #print(check_balanced('4.8+')
    #print(check_balanced('2+3'))
    #print(check_balanced('1+2+3'))    

