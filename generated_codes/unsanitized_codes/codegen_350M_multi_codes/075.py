
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    kare = 3
    a = int(a)
    if kare == 0:
        return True
    if kare == 1:
        b = a * 2.0
        t = a * 3
        s = b * b
        d = kare - 1  # kare + 1
    else:
        n = kare + 1
        b = a * n
        c = 2 * e * k
        m = b * b
        d = c / m

        n = kare - n
        e = d / (k * n * m)
        f = c * n * m
        h = n * m

    u = a * kare - a * d
    v = n * kare - n * e
    w = n * h - n * d * kare

    f = u / v
    d = v / w
    c = b * d * d

    k = kare + 1
    kd = k * k

    g = 3 * kd + c
    f = a * (f + g) + m
    d = a * (d + g) + m
    e = a * (e + g) + m
    h = a * (h + g) + m
    i = b * (i + g) + m
    j = a * (j + g) + m

    k = kd / (d + e + g)
    c = (a * (f + e)) + b * (h + m)
    a = a * c

    e = (a * (e + f)) + (c * (i + d)) + (m * (j + g)) + (c * (h + m))
    b = a * e

    a = a * d /