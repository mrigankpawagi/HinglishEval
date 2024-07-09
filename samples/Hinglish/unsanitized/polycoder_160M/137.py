
def compare_one(a, b):
    """
    Ek function banao jo integers, floats, ya strings jo real numbers ko represent karte hain, leta hai aur usme se bada variable uske diye gaye variable type mein return karta hai.
    Agar values equal hain to None return karo.
    Dhyan do: Agar ek real number ko string ke roop mein represent kiya gaya hai, to floating point . ya , ho sakta hai.

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """   a1, a2 = _eval_to_integer(a)
    b1, b2 = _eval_to_integer(b)
    a1p1, a2p1, b1p2, b2p1 = _get_one(a1, b1)

    e = np.equal
    u = np.asarray(np.real)
    v = np.asarray(np.imag)
    n = len(u) * len(v)

    u_array = np.array([[0, b2p1, b1p1], [-0, a2p1, b2p1], [0, -a2p1, b1p1]])
    v_array = np.array([[0, a2p1, -a1p1], [0, b1p1, a1p1]])

    p = 0
    for m in range(n):
        q = np.asarray(np.real)

        if m == 4:
            p = (p * 2) * a1p1 +