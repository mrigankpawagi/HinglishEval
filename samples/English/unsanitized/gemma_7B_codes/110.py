
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
    if lst2 == []:
        return "NO"
    result = []
    diff = 0
    for i in range(0, len(lst1)):
        diff = diff + lst1[i] - lst2[i]
    if lst1[0] % 2 == 0:
        if diff == 0:
            if lst2 == []:
                return "NO"
    else:
        lst1[i], lst2[i] = lst2[i], lst1[i]
        if diff != 0:
            if diff % 2 != 0:
                return "NO"
            else:
                diff += 2
    if diff == 0:
        return "YES"
    else:
        return "NO"
    #return ''


def main():
    n = int(input())
    lst1 = list(map(int, input().strip().split()))
    m = int(input())
    lst2 = list(map(int, input().strip().split()))
    print(exchange(lst1, lst2))


main()
