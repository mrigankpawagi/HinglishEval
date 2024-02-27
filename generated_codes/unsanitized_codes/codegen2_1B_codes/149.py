
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
    for i in lst:
        for j in lst:
            if i > j:
                lst.remove(i)
    return lst
<|python|>#