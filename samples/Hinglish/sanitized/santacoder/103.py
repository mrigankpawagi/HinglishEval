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
    res = ""
    if n <= 0:
        return -1
    n0 = n / 2 * 2 + 1 if n % 2 == 1 else n / 2 * 2

    if m > n0 and n0 / 2 * 2 < m:
        return -1

    while n0 >= m:
        m = n0
        n0 = n0 / 2

    if n0 <= m / 2 and m / 2 * 2 > n0:
        m = m / 2

    if n0 + 1 <= m / 2 and m / 2 * 2 < n0 + 1:
        m = m / 2
    i = 1
    j = n0
    while i * 2 <= n0:
        i = i * 2 + 1
        if j / i > m:
            return -1
        j = ((n0 - i) * j + i * j) / 2

    s = ""
    q = n0 // 3 + 1
    # print(n0, j, m, m - n0, q * 3)
    while m - n0 < q * 3:
        s = "0b" + s
        m -= q * 3
        q = 0 if m == 0 else q + 1

    s += "1"

    return s
