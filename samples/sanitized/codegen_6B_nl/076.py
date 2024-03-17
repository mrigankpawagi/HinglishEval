
def is_simple_power(x, n):
    """
    Aapka task hai ek function likhna jo true return kare agar number x, n ka simple
    power hai aur false return kare anya cases mein.
    x n ka simple power hai agar n**int=x
    Jaise ki:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """

    m, k = [1], [1]
    for i in range(int(n**0.5), int(n**2), -1):
        if is_power_of_2(i) == 1:
            m.append(i**0.5)
            k.append(1)
        elif is_power_of_2(i) == 0:
            m.append(2**(i + 1))
            k.append(0)
        else:
            print(2)

    print([i for i in m if i**n == x])
