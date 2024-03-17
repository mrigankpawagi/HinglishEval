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
    """
    word_list = []
    s = s.lower()
    for x in range(n):
        word_list.append("")
    for letter in range(len(s)):
        if letter != 0 and letter != len(s) - 1:
            if (s[letter - 1] + s[letter + 1]).isalpha() == False:
                word_list[x] = word_list[x] + s[letter]
    print(str(word_list).replace("[", "").replace("]", "").strip())