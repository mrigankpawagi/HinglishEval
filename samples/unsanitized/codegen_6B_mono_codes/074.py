
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
    if len(lst1)==0 or len(lst2)==0:
        return []

    if len(lst1)==len(lst2):
        return lst1

    return []

assert total_match([], []) == []
assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']



