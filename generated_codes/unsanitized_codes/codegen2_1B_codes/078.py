
def hex_key(num):
    """
    Aapko ek function likhna hai jo ek hexadecimal number ko string ke roop mein leta hai aur ginata hai ki kitne hexadecimal digits prime hain (prime number, ya prime, ek natural number hota hai jo 1 se bada hota hai aur do chote natural numbers ka product nahi hota).
    Hexadecimal digits hote hain 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers hote hain 2, 3, 5, 7, 11, 13, 17,...
    To aapko ye determine karna hai ki nimn digits ki sankhya kitni hai: 2, 3, 5, 7, B (=decimal 11), D (=decimal 13).
    Note: aap maan sakte hain ki input hamesha sahi ya empty string hoga, aur symbols A,B,C,D,E,F hamesha uppercase mein honge.
    Examples:
    Agar num = "AB" hai to output 1 hona chahiye.
    Agar num = "1077E" hai to output 2 hona chahiye.
    Agar num = "ABED1A33" hai to output 4 hona chahiye.
    Agar num = "123456789ABCDEF0" hai to output 6 hona chahiye.
    Agar num = "2020" hai to output 2 hona chahiye.
    """
    result = "0"*(num.__len__()//2)

    for i in range(len(num)):
        if num[i] == "0":
            return i % len(num)

    for i in range(len(num)):
        cnt = 0
        for j in range(num[i].__len__()//2):
            if num[i][j] == "0":
                cnt += 2
        if cnt!= 0:
            return i % len(num)


<|python|>
import time
import socket