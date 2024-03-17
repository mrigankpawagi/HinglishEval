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
    if len(lst1) == 0 or len(lst2) == 0:
        return []

    tmp_list1 = lst1.copy()
    tmp_list2 = lst2.copy()

    res = []
    while len(tmp_list1) != len(tmp_list2):
        if len(tmp_list1 + res) > len(tmp_list2):
            tmp_list1.append(tmp_list2[0])
            tmp_list2.pop(0)
        else:
            tmp_list1.append(tmp_list2[len(tmp_list1)])
            tmp_list2.pop(len(tmp_list1))

    return res
