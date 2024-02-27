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
    def up(n):
        prime = [1]
        for i in range(2, n):
            for p in prime:
                if p == 2:
                    prime.append(3)
                elif p == 3:
                    prime.append(5)
                elif p == 5:
                    prime.append(7)
                elif p == 7:
                    prime.append(11)
                elif p == 11:
                    prime.append(13)
                elif p == 13:
                    prime.append(17)
                elif p == 17:
                    prime.append(19)
                else:
                    prime.append(p)
        return prime
    up_list = []
    for i in range(0, n + 1):
        up_list.append(up(i))
    return up_list