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
    even_lst1 = [num for num in lst1 if num % 2 == 0]
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    if sum(even_lst1) % 2 == 0:
        return "YES"
    elif sum(even_lst1) % 2 != 0 and sum(even_lst2) % 2 == 0:
        return "YES"
    else:
        return "NO"
