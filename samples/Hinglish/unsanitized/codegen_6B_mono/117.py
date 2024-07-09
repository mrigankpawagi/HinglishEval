
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
    import re
    regex = re.compile(r'[^aeiouAEIOU]')
    n_letters = [re.sub('[^aeiouAEIOU]',r'',string.lower()) for string in re.findall(regex, s)  ]
    words = list(filter(len,set(n_letters)))
    if len(words) > (n):
        return words[:n]
    else:
        return words



# This is the solution of above problem, with one small change.
# In this, we first convert input s to lowercase string then we split it up and convert it in list.
# Then we use the filter function to get the unique values.

