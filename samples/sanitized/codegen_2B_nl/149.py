
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
    lst_len = len(lst)
    if not lst_len: return []

    def word_sum(word_list):
        """
        Iterate over the specified list of words; each time through the loop we
        add the number of occurences of each word in the list to a global
        variable `counts`. The list of words is passed in as an argument, and a
        global `remaining_words` variable is used to capture the rest of the
        words we've yet to iterate over in the list. Finally, return a list of
        all the words in the word list.
        `remaining_words` is an appropriate type for keeping track of the last
