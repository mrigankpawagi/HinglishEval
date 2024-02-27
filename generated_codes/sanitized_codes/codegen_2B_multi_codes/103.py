
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
    # check if m is not negative
    if m < 0:
        raise ValueError("invalid arguments")
    if (m & (m - 1)):
        raise ValueError("invalid arguments")

    n = int(round(n, 0))
    n1 = n >> 1
    m1 = m >> 1
    # we have 2 cases. for m < n, we need to take
    # all integers n1 to 2N2+1
    # for m >= n, we need to take all integers 
    count1 = 0
    if n == 0:
        yield "0b00"
    else:
        if m >= n:
            for i in range(1, m+1):
                yield "0b" + str(count1)
                count1 += 1
        else:
            if m == 1:
                yield "0b0"
            elif m == 3:
                yield "0b100"
            for i in range(n1, min(n2, n-1, SENTINEL)):
                yield "0b" + str(count1)
                count1 += 1

