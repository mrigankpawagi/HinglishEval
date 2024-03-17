def count_up_to(n):
    """
    Ek function implement karo jo ek non-negative integer leta hai aur return karta hai ek array jisme pehle n
    integers hote hai jo prime numbers hai aur n se kam hai.
    Jaise ki:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    res = []
    n = int(n)
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res