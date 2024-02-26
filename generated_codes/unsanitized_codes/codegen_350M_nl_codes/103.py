
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
    n, m = int(n), int(m)
    n = n/2
    if n%2 == 0 and n%2 < 2 and n % 2 == 0 :
        return n*round(n/2,10)

    result = None
    for i in range(n*n//2 + 1, n):
        result = round(math.signum(n*math.log10(i/2)), 2)

    return round(result,10)


