
def prime_length(string):
    """
    Ek function likho jo ek string leta hai aur return karta hai True agar string 
    ki length ek prime number hai ya False otherwise
    Udaharan
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) <2:
        return False
    def find_prime(number):
        if number < 2:
            return False
        for i in range(2,number):
            if number % i ==0 :
                return False
        return True
    return find_prime(len(string))
print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))

# question 2

def is_prime_num(num):
    """
    Ek function likho jo paara number(int)
    Lela hai aur True return karta hai agar number prime hai
    false otherwise
    
    Udaharan
    is_prime_num(1) == True
    is_prime_num(97) == True
    is_prime_num(43) == False
    """
    if num <2:
        return False
    for i in range(2,num):
        if num %i == 0:
            return False
    return True
num = int(input("Enter number: "))
print(is_prime_num(num))





# question no. 3

def anagram_checker(string_a,string_b):
    """
    Ek function likho jo ek do jayegi string
    and anagram_checker('a','b') == False
    anagram_checker('ma' ,'aam') == True
    """
    for string_a, string_b in zip(word,word_b):
        if len(string_a) != len(string_b):
            return False
    return True

word = input("Enter first String: ")
word_b = input("enter second string: ")
print(anagram_checker(word,word_b))
