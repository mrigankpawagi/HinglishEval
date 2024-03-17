
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
    n = int(n)
    m = int(m)
    m = 2 ** m
    rounded = b''\
        b'\x00' if n == 0 else b'\x01'
    return "%d %d" % (m * n, b''.join(
        "%d %d" % (k for k in b) for b in zip(b'\x01' * k, b''.join(b) for b in (n, m))))

