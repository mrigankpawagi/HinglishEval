
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
    while m > 0:
        n /= 2
        m -= 1

    if m == 0:
        return ('0b' + bin(n)[2:]).replace('0', '5')
    else:
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
