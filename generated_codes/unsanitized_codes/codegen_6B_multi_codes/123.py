
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
    return [x for x in collatz_sequence(n) if x.is_odd()]

assert get_odd_collatz(7) == [1]
# assert get_odd_collatz(1) == [1]
assert get_odd_collatz(12) == [1, 3, 5, 9]
# assert len(get_odd_collatz(11)) == 2

