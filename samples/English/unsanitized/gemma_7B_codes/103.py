
def rounded_avg(n, m):
    """
    Aapko do positive integers n aur m diye gaye hain, aur aapka task hai n se lekar m tak ke integers ka
    average compute karna (n aur m ko bhi include karte hue). 
    Answer ko nearest integer tak round karo aur usko binary mein convert karo.
    Agar n m se bada hai, to -1 return karo.
    Udaharan:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    # YOUR CODE HERE
    a=round(sum(range(n,m+1))/(m-n+1))
    b=bin(a).replace("0b","").zfill(4)
    if n>m:
        b="-1"
    else:
        b
    return 

# Question 2

def add_binary(a, b):
    """
    This question will be interesting if you have done question 1.
    Aapko do integers a aur b diye gaye hain. 
    Har iske binary representation mein jo digitize wale saare digits add karo aur jo digits (decimal mein) aaye those ko binary mein convert karo.
    Udaharan:
    add_binary(1, 2) => "0b5"
    add_binary(4, 8) => "0b10"
    add_binary(9, 11) => "0b22"
    add_binary(5, 9) => "0b13"
    """
    # YOUR CODE HERE

def compare(a,b):
    """
    Aapko do strings a aur b diye gaye hain.
    Aapko dunga a ke char mein usne "0b " jo daal dala hai, aur ussey delete karne ko bolunga.
    To yeh dono ko compare karo.
    Udaharan:
    compare("0b10", "0b1") => "0b10" hai 
    compare("0b100", "0b1") => "0b1" hai
    """
    # YOUR CODE HERE

# Question 3

def all_factors(n):
    """
    Aapko ek positive integer n dia gaya hai.
    Aapko apne aap n se aur un integers se compute karne ka kaam ho gaya ye kisi bhi number ko divide kar sakte hain.
    These are the factors of n. 
    Udaharan: all_factors(6) => "2 3"
    """
    # YOUR CODE HERE

# Question 4
from operator import xor

def one_xor_zero(n):
    """
    Aapko ek integer n de dia gaya hai.
    Aapko ap