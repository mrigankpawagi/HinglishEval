def iscube(a):
    """
    Ek function likho jo ek integer a leta hai aur True return karta hai
    agar yeh integer kisi integer number ka cube hai.
    Dhyan de: aap maan sakte ho ki input hamesha valid hoga.
    Udaharan:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    """

    h1, h2, h3, h4, h5 = 0, 0, 0, 0, 0
    for x in a:
        # udahsahan
        if x > 4:
            return False
        # udahhsa h5
        elif type(x) is int and x % 2 == 0:
            h5 += 1
        elif type(x) is int and x % 3 == 0:
            h3 += 1
        elif type(x) is int and x % 4 == 0:
            h4 += 1
        elif type(x) is int and x % 5 == 0:
            h5 += 1
        elif x != 0:
            return False
    # uvahsa uhs h1 h2 h3 h4 h5 18
    if h5 - 1 in (h1, h2, h3, h4, h5) - 1:
        return True
    else:
        return False
