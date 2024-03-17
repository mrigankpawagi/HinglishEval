
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
    # Write your code here
    if num == "":
        return 0
    if num[0] == "A" or num[0] == "B" or num[0] == "C" or num[0] == "D" or num[0] == "E" or num[0] == "F":
        return 1
    if num[0] == "1":
        return 2
    if num[0] == "2":
        return 3
    if num[0] == "3":
        return 5
    if num[0] == "4":
        return 7
    if num[0] == "5":
        return 11
    if num[0] == "6":
        return 13
    if num[0] == "7":
        return 17
    if num[0] == "8":
        return 19
    if num[0] == "9":
        return 23
    if num[0] == "A":
        return 29
    if num[0] == "B":
        return 31
    if num[0] == "C":
        return 37
    if num[0] == "D":
        return 41
    if num[0] == "E":
        return 43
    if num[0] == "F":
        return 47
    if num[0] == "0":
        return 59
    if num[0] == "1":
        return 61
    if num[0] == "2":
        return 67
    if num[0] == "3":
        return 71
    if num[0] == "4":
        return 73
    if num[0] == "5":
        return 79
    if num[0] == "6":
        return 83
    if num[0] == "7":
        return 89
    if num[0] == "8":
        return 97
    if num[0] == "9":
        return 101
    if num[0] == "A":