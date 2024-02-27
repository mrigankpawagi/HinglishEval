def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # gcd(a+b,-a-b) = 0 : r_i = (a+b)/(a-b) #r^2 + r[1]x + r[2]x + r[3]x + r[4]x +... + r[a_n]x + r[a_n]+1 = 0
    # r^2 + r[1]x + r[2]x + r[3]x + r[4]x +... + r[n]x + r[n]+1 - a-b = 0 ;
    # r^2 + r[i]x - a-b = 0.
    # a+b - a-b = -b - a
    # -b + a = a-b
    r = [0] * len(str())
    for j in range(b, -a - b, -b):
        karo = j
        # print(j)
        r[karo] = j
    for j in range(2, len(str())):
        karo = 0
        # print(r)
        while r[karo] != -1:
            if r[karo] == -1:
                break
            if r[r[karo]] - r[karo] == 1:
                r[karo] -= 1
            elif r[r[karo]] > r[karo]:
                r[karo] = r[r[karo]] - r[karo]
            else:
                karo = r[karo]

        r[karo] = -1
    return sum(r)


a = 1234567890
b = 2345678910

print("greatest common divisor - %s" % greatest_common_divisor(a, b))

# r = []
# hx =
