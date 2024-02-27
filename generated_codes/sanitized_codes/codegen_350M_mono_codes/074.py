def total_match(lst1, lst2):
    """
    Ek function likho jo do string ki lists ko accept kare aur woh list return kare jisme
    total number of chars saare strings me dusre list se kam ho.
    Agar dono lists me same number of chars ho, toh pehli list return karo.
    Udaharan
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    """
    dict1 = dict()
    dict2 = {}
    for i in lst1:
        for j in lst2:
            if i == j:
                dict1[i] = len(i)
    return list(dict1.values())