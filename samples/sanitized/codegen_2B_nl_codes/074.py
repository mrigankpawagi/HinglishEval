
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

    if len(lst1)!= len(lst2) or lst1 is None or lst2 is None:
        return [lst1, lst2]
    else:
        # Calculate length of longest string in the first list.
        len1 = len(lst1)
        if len(len1):
            # Length is present in the 1st list.
            num1 = len1
        else:
            # Length is absent in the 1st list but is present in the second.
            len2 = len(lst2)
            if len2!= 0:
                # If the list-1 has a length,