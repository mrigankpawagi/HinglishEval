
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
    if n * m == 0: #Division by 0
        return -1
    return str(int(round(n * m / 100)))


