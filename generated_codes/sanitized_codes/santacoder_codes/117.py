
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
    consonants = ['a', 'e', 'i', 'o', 'u']
    words = []
    # m = m_lower + m_upper
    l = m_lower
    # m = [l[0]] + m_lower + m_upper + m_space + m_number + m_other + m_space
    # m + s

    for i in consonants:
        
        if l[-1] == l[:-1] and l[:-1] in m_length:
            
            #print("list" + ".append(str(ord(i)))")
               
            words+=[i]

            l_ = l + l_

            l = l_[:-1]

        elif i in l:
            words+=[i]
            l=l[:-1]

    # print("len")
    # print(len(words))

    # karkondo konsonants word se list mein ek list
    new_words = []

    new_words = words.copy()

    if len(new_words) < n:
        #print("new_words")
        #print(new_words)
        print("number of the number of words in input string is less than the karna hai")

    s_copy = s.copy()

    i=1

    while i <= n:
       