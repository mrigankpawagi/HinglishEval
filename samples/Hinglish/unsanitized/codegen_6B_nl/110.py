
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
    res = ""
    in1, in2 = lst1, lst2
    if (not in1) or (not in2):
        return res
    for number in in1:
        if in2.count(number) == 0:
            in2.remove(number)
        elif in2.count(number) == 1:
            in2.remove(number)
            in2.append(number)
        else:
            pass
    for number in in2:
        if in1.count(number) == 0:
            in1.remove(number)
       