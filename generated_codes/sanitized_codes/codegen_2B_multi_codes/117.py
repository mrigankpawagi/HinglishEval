
def select_words(s, n):
    """
    Ek string s aur ek natural number n diya gaya hai, aapko ek function implement karna hai jo 
    string s se exactly n consonants wale saare words ko ek list mein return kare, jis order mein ye words string s mein appear hote hain.
    Agar string s khali hai to function ko ek khali list return karni chahiye.
    Note: Aap maan sakte ho ki input string mein sirf letters aur spaces honge.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """   words = copy.deepcopy(s.split(""))
    letters_count = 0
    word_list = []
    for word in word_iter(s):
        if str.isalpha(word):
            letters_count += 1
        word_list.append(word)

    if letters_count < n:
        return []
    elif letters_count == n:
        return word_list
    else:
        return random.sample(word_list, n - letters_count)
