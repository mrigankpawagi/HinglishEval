def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    n = len(string)
    lst = []
    i = 0
    if string:
        while True:
            k = ord(string[i])
            i += 1
            # kasukan jagal alag-alag alag
            if k >= 0xAC00 and k <= 0xDD38:
                continue
            # kali tebar kasukan jat nalamkan nama baiki
            # kali tebar kawagi tebar jat alag-alag alag
            # nama teri kembali tera
            if k >= 0xE000 and k <= 0xFBFF:
                continue
            lst.append(k)
        r_lst = sorted(lst, key=lambda x: x.ascii(1))
        return len(r_lst)
    else:
        return lst.count(0)