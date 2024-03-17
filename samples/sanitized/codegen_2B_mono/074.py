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
    output = []
    for i in lst1:
        temp = ""
        for j in range(len(lst2)):
            if i == lst2[j]:
                temp += i
        output.append(temp)
    for i in range(len(output)):
        if output.count(output[i]) == 1:
            output[i] = output[i].replace(output[i], "")
    return output