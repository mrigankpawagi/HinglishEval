
def exchange(lst1, lst2):
    """
    Is problem mein, aapko ek function implement karna hai jo do list of numbers leta hai,
    aur yeh determine karta hai ki kya inke beech elements ka exchange karke
    lst1 ko sirf even numbers ki list banaya ja sakta hai.
    lst1 aur lst2 ke beech exchanged elements ki sankhya par koi limit nahi hai.
    Agar lst1 aur lst2 ke beech elements exchange karke
    lst1 ke saare elements ko even banaya ja sakta hai, to "YES" return karo.
    Varna, "NO" return karo.
    Jaise ki:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    Maan liya jata hai ki input lists khali nahi hogi.
    """
    if len(lst1)!= len(lst2):
        #print("Exchange cannot cross the list lengths!")
        raise Exception("Exchange cannot cross the list lengths!")

    diff_list = list(set(lst1) - set(lst2))
    if len(diff_list)!= 0:
        return "NO"
    else:
        if len(lst1) - len(lst2) == 1:
            return "YES"
        else:
            return "no"
            
