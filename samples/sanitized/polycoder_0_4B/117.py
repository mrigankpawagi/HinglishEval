
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
    # hao se kare hayi kein, ye wate hayi hai taha aamah
    s = []
    r = s.append
    for a in "ka: " + ye_char:
        for j in "noki kain hey hai bushi lamb":
            if a not in r:
                s.append(j)
                break
    s = "".join(s)
    if n == 1:
        s = s
    elif n == 2:
        h = ""
        for j in "noki kain hey hai bushi lamb":
            if a == "ka" or a == "ka" or j