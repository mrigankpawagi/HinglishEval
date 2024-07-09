
def check_if_last_char_is_a_letter(txt):
    """
    Ek function banaiye jo True return kare agar diye gaye string ka last character ek alphabetical character ho aur wo kisi word ka hissa na ho, anyatha False return kare.
    Dhyan de: "word" ek characters ka group hota hai jo space se alag na ho.

    Udaharan:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("") ➞ False
    """
    if not len(txt): return False
    c_num = len(txt) - 1
    if txt[c_num]!= key_list.get(txt[c_num], '#'):
        return False
    return True

check_if_last_char_is_a_letter(test_case_one = 'apple pie', test_case_three = 'apple pi e')

The problem is I do not want to use a big list, I want use a dictionary. How to access the list in a dictionary. The list in dictionary is "key" and the value is the list.

A:

I had a look at the docs, you could use key directly as a function. That said if you want to use list()/len() you could also do this:
test_case_one = "apple pie"
test_case_three = "apple pi e"
txt = []
txt.append('%s'%test_case_one)
txt.append('%s'%test_case_three)
key_list = d['txt']
key_list.append(test_case_one)
key_list.append(test_case_three)

So if your key_list is d['txt'] then d['txt'][0] = test_case_one and d['txt'][1] = test_case_