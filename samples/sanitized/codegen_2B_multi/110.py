
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
    if lst1 == lst2:
        return yes
    else:
        a = []
        for i in range(len(lst1)):
            if i == 0 or lst1[i]!= lst1[i-1]:
                lst1[i] = (lst1[i]+lst1[i-1]) % 10
            else:
                a.append(lst1[i])
                lst1[i] = lst2[i]
            for j in range(len(lst2)):
                if j == 0 or lst2[j]!= lst2[j-1]:
                    lst2[j] = (lst2[j]+lst2[j-1]) % 10
                else:
                    a.append(lst2[j])
                    lst2[j] = lst1[j]

        while len(a)!= 0 and lst2[len(lst2)-1] == 0:
            lst2.pop()
        if len(lst1) == len(lst2):