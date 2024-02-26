
def get_odd_collatz(n):
    """
    Diye gaye positive integer n ke liye, ek sorted list return karo jo collatz sequence mein odd numbers ko contain karti ho.

    Collatz conjecture ek mathematics ka conjecture hai jo ek sequence ke baare mein baat karta hai
    jise is prakar se define kiya gaya hai: kisi bhi positive integer n se shuru karo. Phir har term ko 
    previous term se is prakar se prapt kiya jata hai: agar previous term even hai, toh next term 
    previous term ka aadha hota hai. Agar previous term odd hai, toh next term 3 guna previous
    term plus 1 hota hai. Conjecture yeh hai ki chahe n ki value kuch bhi ho, sequence hamesha 1 tak pahunchegi.

    Note: 
        1. Collatz(1) is [1].
        2. returned list badhat kram mein sorted hoti hai.

    Jaise ki:
    get_odd_collatz(5) returns [1, 5] # 5 ke liye collatz sequence [5, 16, 8, 4, 2, 1] hai, toh odd numbers sirf 1, aur 5 hai.
    """
    if n <= 1:
        return [n] # 0, 1, 2, 3, 4, 5 is hota hai - collatz n aur liye.
    
    odd_collatz = list()
    odd_collatz.append(n)
    for i in range(1, n):
        current_odd = 2 * odd_collatz[i // 2] + (int(odd_collatz[i // 2]) == int(odd_collatz[i // 2]) -1)
        if (not i //2 in odd_collatz):
            odd_collatz.append(current_odd)
        
    # Oddeven sequence hari ki karo har jata hai, toh next odd sequence tadi 3 guna odd hur. [