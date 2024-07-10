
def check_if_last_char_is_a_letter(txt):
    """
    Ek function banaiye jo True return kare agar diye gaye string ka last character ek alphabetical character ho aur wo kisi word ka hissa na ho, anyatha False return kare.
    Dhyan de: "word" ek characters ka group hota hai jo space se alag na ho.

    Udaharan:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("") ➞ False
    """
    # print(text)
    # for i in range(len(a)):
    #     if ord(a[i])>=65 and ord(a[i])<=90:
    #         print(a[i],end='')
        # continue
        # else:
    for i in txt:
        if i.isalpha():
            if len(txt)==1:
                return True
            else:
                # print(i," ",len(txt))
                t = i
                l = len(txt)
                return t == txt[l-1]
        # else:
            # return False




# List of test case to run  on your function:
# txt = "pi"
# txt = "appl"
# txt = "appl "
# txt = "apple"
# txt = " apple"
# txt = "apple pi e"
# print(check_if_last_char_is_a_letter(txt))


# Function to test above:-
