
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

    if len(lst1) == 0 and len(lst2) == 0:
        return []


    elif len(lst1) > len(lst2):
        return lst1
    elif lst1 == lst2:
        return lst1
    elif len(lst1) > 1:
        # return lst1[-2:]+lst1[-1] if lst1[0] == lst2[0] and lst1[1] == lst2[1] else []
        match_list=[]
        for x in range(2):
            if lst1[x] == lst2[x]:
                match_list.append(lst1[x])
            else:
                match_list.append("")
        return match_list
    else:
        return [""]



print total_match(['4'], ['1', '2', '3', '4', '5'])

