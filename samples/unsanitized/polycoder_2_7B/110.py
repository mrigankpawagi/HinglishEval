
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
    lst1 = [item for sublist in lst1 for item in sublist]
    lst1 = [item for sublist in lst1 for item in sublist]
    len1 = len([i for sublist in lst1 for i in sublist])
    len2 = len([i for sublist in lst2 for i in sublist])

    if len1 > len2:
        return "NO"
    else:
        result = "YES"
        for i in range(len1):
            l = lst1[i]
            r = lst2[i]
            for k in range(l + 1, r + 1):
                if not k % 10:
 