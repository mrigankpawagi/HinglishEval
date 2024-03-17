
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
    res = set()
    for a in lst2:
        if int(a) not in lst1:
            continue
        else:
            res |= set(lst1)
            res.add(int(a))
    res = set(res)
    for a in lst1:
        if a not in lst2:
            continue
        if not res.issubset(lst2):
            continue
        res &= set(lst2)

    if res:
        return "OK" if res else "KO"
    if lst1 + lst2:
  