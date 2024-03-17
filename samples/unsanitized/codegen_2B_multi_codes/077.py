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
    # return (isint(a) and a <= sys.maxint and a >= 0) or (a == 0)
    return (
        a == 0
        or (a % 3 == 0 and isint(a / 3))
        or (isint(a / 3) and not isint(a / 4))
        or (isint(a / 4) and not isint(a / 8))
        or (isint(a / 8) and not isint(a / 16))
    )
