
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

    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = [0] * 26

    print("hi this is a function")

    print("I got user input")

    for i in range(0, len(s)):

        temp = s[i].capitalize()
        print(s[i] + "=>" + temp)

        count[s[i].upper()] += 1

    letters_found = 0

    for i in range(len(s)):

        if(count[s[i].upper()] > 0):            #Check if this letter was seen in the string

            letters_found = letters_found + 1

            #letter = str(temp) #I tried this but its not working

    print(letters_found)       
