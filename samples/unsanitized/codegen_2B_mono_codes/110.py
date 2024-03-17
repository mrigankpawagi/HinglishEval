
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

    res_list = list()
    while lst1 or lst2:
        if lst1[0] % 2!= 0 and lst2[0] % 2!= 0:
            res_list.append(lst1[0])
            lst1.pop(0)
            lst2.pop(0)

        elif lst1[0] % 2!= 0 and lst2[0] % 2 == 0:
            if lst2 or lst2!= []:
                lst2.pop(0)
            lst1.append(lst1[0])
            lst1.pop(0)

        else:
            if lst1[0] % 2 == 0 and lst2 or lst2!= []:
                lst2.pop(0)
            lst1.append(lst1[0])
            lst1.pop(0)

    if len(res_list) == 0:
        return "NO"
    else:
        return "YES"


print(exchange([1, 2, 3, 4], [3,