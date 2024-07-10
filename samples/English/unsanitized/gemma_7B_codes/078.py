
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
    return -1

def binary_to_hex(b_num):
    """
    Aapko ek function likhna hai jo binary number ko hexadecimal number mein badalte hai.
    Aapko us number ke ek representation ko hi return karna hai jaana hi possible hai.
    This question is inspired by an excellent discussion on Stack Overflow, which you can refer to if you’d like. To save you any click effort (and to prevent copyright issues), here’s a screenshot of that discussion:https://lh3.googleusercontent.com/768G3kK-Y1kH_f_x2X3j47pZvR-Z7vW5X76799gD77917D6954572243749D132C6B7A5C7568213B602A10B6A65317243B=h550-rw
    Examples:
    Agar b_num = 1101 hai to output 8 (hexadecimal decimal for 1101 in binary is 8) hona chahiye.
    Agar b_num = 125 hai to output 7D (hexadecimal decimal for 7D in binary is 125) hona chahiye.
    Agar b_num = 1001 hai to output 12 (hexadecimal decimal for 1001 in binary 1001 is 12) hona chahiye.
    Agar b_num = 1022 hai to output 372 (hexadecimal decimal for 1022 in binary is 372) hona chahiye.
    Agar b_num = 33534 hai to output 807C (hexadecimal decimal for 807C in binary is 33534) hona chahiye.
    """
    return -1

def decimal_to_hex(decimal):
    """
    Aapko is question ka naam hi samajh a jayaga: us function likhna hai jo decimal number ko hexadecimal number mein badalta hai. Ye function decimal ko decimal mein nahi, hex integer mein badalta hai.
    Aap