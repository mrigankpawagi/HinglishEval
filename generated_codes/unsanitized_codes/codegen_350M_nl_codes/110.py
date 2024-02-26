
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

    exchange_str = '''
    aapko jhayo ek ko exchange function karna hai jo do lst1 ko saare
    ko niye saare loh kya beech elements ke karke karke lst2 ko sirf
    lst1 ko sirf even numbers ki kharif limit nahi hai.
    lst1 azl mnei.
    kara kara hai niye aapko ek ko kya exchange karke ko nahi banaya
    samy ko samy loh kya beech elements ko saare nahi hogi.
    '''

    exchange_list = '[' + input_list + '] [' + exchange_str + ']'
    exchange_list.extend(lst1)

    return exchange_list


