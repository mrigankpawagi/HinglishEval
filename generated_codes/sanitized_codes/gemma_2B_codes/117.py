
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
    # Your code here
    if len(s) == 0:
        return []
    else:
        list_of_words = []
        for i in range(len(s)):
            if s[i].isalpha():
                list_of_words.append(s[i])
        list_of_words.sort()
        return list_of_words[n:]
