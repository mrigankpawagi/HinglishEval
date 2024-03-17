
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

    if len(s.lower()) > 0:
        str_data = s.lower()
        str_data_list = [i for i in str_data if i!='']
        str_data_list = filter(None, str_data_list)

        #str_data_list = s.split()
        #print("Length is ",len(str_data_list),".")
        print(len(str_data_list))

        #list_data =[]
        #for i in str_data_list:
        #    list_data.append(i)
        list_data = str_data_list
        while len(list_data) < n:
            list_data.append(" ")
   