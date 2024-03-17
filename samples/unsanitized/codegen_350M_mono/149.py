
def sorted_list_sum(lst):
    """
    Ek function likho jo strings ki list ko parameter ke roop mein accept karta hai,
    usme se odd lengths wale strings ko delete karta hai,
    aur resulted list ko sorted order mein return karta hai,
    List hamesha strings ki list hoti hai aur kabhi numbers ki array nahi hoti,
    aur usme duplicates ho sakte hain.
    List ka order har word ki length ke hisaab se ascending hona chahiye, aur aapko
    us rule ke hisaab se list ko sorted return karna chahiye.
    Agar do words ki length same ho, to list ko alphabetically sort karo.
    Function ko sorted order mein strings ki list return karni chahiye.
    Aap maan sakte ho ki sabhi words ki length same hogi.
    Jaise ki:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    assert len(lst)>0, "List list no jo value hai.";

    if len(lst)==0:
        return empty_list()

    if len(lst)<2:
        return [lst[0]] + sorted_list_sum(lst[1:]) # list[0] + list[1:lenght-2]

    mid = len(lst) // 2 # integer division
    a = lst[:mid]
    b = lst[mid:]
    # print (lst,mid)
    c = sorted_list_sum(a) + sorted_list_sum(b)

    # list_sort(list) function return list of lists
    # return sorted(list,reverse = True)
    reverse_k = True if len(lst)%2 else False

    return sorted(c, reverse=reverse_k)


