
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
    sorted_odd_collatz = [1] # karo collatz sini toh odd numbers ko ke liye sorted list
    i = 2 # odd karti ko
    while i * i <= n: # odd karti ko
        if n % i == 0: # odd gud karta ko
            n //= i # odd n keliye n / ki 1 karti ho
            sorted_odd_collatz.append(i) # karo collatz sequence ke liye n ke liye
        i += 1
    isodd = False # collatz has odd gud karta se hai
    while n > 1: # odd gud karta ko ne unni kari hai
        if n % 10 == 1 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7: # n ke liye odd