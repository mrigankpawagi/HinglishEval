
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

    # if len(lst1) == len(lst2):
    #     if all(x == y for x, y in zip(lst1, lst2)):
    #         return "YES"

    #     counter3 = 0
    #     for x in range(len(lst1)):
    #         for y in range(len(lst2)):
    #             if lst1[x] > lst2[y]:
    #                 for i, j in zip(lst1, lst2):
    #                     if i > j:
    #                         lst1.insert(counter3 + x, j)
    #                         lst1.remove(i)
    #                         lst2.remove(j)
    #                         break
    #                     elif i < j:
    #                         lst1.insert(counter3 + x, i)
    #                         lst1.remove(i)
    #                         lst2.remove(j)

    #         for x in range(len(lst2)):
    #             if lst2[x] > lst1[x]:
    #                 for i, j in zip(lst1, lst2):
    #                     if i > j:
    #                         lst1.insert(counter