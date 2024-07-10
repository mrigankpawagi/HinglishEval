
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
    # 2 List ko compare karenge aur woh string return karo jo
    # usse less number of characters contain
    # agar same character hain toh usse chota size wala return karo
    # ucharan
    # total_match(['4']) -> ['4']
    # total_match(['1', '2']) -> ['1', '2']
    # total_match(['1', '2', '3']) -> ['1', '2', '3']
    # total_match(['1', '2', '3', '4']) -> ['1', '2', '3'] -> ['1', '2', '3', '4']
    # total_match(['4'], ['1', '2', '3', '4', '5']) -> ['4']
    
    # 1 method 
    import copy
    if len(lst1) == len(lst2):
        lst1.sort(key=len)
        lst2.sort(key=len)
        lst1 = lst1[::-1] if lst1[0] > lst2[0] else lst1
        return lst1
    lst2 = copy.copy(lst2)
    if len(lst1) > len(lst2):
        for i in range(min(len(lst1), len(lst2))): 
            if len(lst1[i]) < len(lst2[i]):
                lst1 = lst1[i:] + lst2[:i]
                return lst1
    else:
        for i in range(min(len(lst1), len(lst2))):
            if len(lst1[i]) > len(lst2[i]):
                lst2 = lst2[i:] + lst1[:i]
        return lst2
       
    # 2 method 1
    def find_len(lst):
        return [len(val) for val in lst]
    m = {find_len(lst1): lst1, find_len(lst1): lst2}
    if len(m)== 1:
        return m[min(m.keys())]    
      
    # 2 method 2
    m = {x: y for x, y in zip(find_len(lst