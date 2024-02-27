
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
    for i in lst1[::-1]:
        if i % 2 == 0:
            lst1.pop()
            lst2.insert(0, i)
    if lst1 == lst2:
        return 'YES'
    return 'NO'


# def checkio(list1, list2):
#     try:
#         if len(list1) == len(list2):
#             for i in [x for x in zip(list1, list2) if x[0] == x[1]]:
#                 list1.remove(i[0])
#                 list2.remove(i[1])
#             return 'YES'
#         else:
#             return 'NO'
#     except (IndexError, ValueError):
#         return 'NO'
#     except (Exception) as e:
#         return 0

