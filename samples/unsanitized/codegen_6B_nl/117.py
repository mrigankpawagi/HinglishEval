
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
    words = []
    # check for number of valid characters in a string
    length_of_string = len(s)
    number_of_consonants = 0
    if length_of_string == n:
        words = s
    else:
        while length_of_string > number_of_consonants:
            if s[number_of_consonants] == s[number_of_consonants + 1]:
                words += [s.replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "")]
            words += s[number_of_consonants:]
            number_of_consonants += 1
    if number_of_consonants > n:
    