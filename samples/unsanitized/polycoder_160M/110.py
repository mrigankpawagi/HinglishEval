
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

    n = 100

    karka, kara, kara = list(map(exchange, lst1))

    for i in range(n):
        if i == 0:
            yield True
        else:
            for ai in karka:
                if list(ai).index(i) == i:
                    yield {"kara.bak.vac.kara.kara.kara":"{i}:" + ",{ai}":-10, :(bak.vac.bak.vac.kara.kara.kara.kara,"!{}".format(*akara))}.replace("kara.%i.%i" % (i+1, i