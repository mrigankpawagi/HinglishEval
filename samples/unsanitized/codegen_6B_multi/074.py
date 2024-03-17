
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
    
    if not lst1 or not lst2:
        return []

    common = []
    count = Counter()
    for lst in list(lst1):
        if lst in count:
            count[lst] += 1 
        else:
            count[lst] = 1
    for lst in list(lst2):
        count[lst] -= 1
        if count[lst] == 0:
            common.append(lst)
    return common
    
