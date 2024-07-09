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
    for s in lst1:
        total_match(s, [])
        total_match(s, ["hi\n"])
        total_match(s, ["4"])
    for s in lst2:
        total_match(s, [])
        total_match(s, ["hi", "admin"])
        total_match(s, ["hI", "Hi"])
        total_match(s, ["4"])