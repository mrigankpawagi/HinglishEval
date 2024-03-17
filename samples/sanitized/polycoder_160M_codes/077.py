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
    if type(a) == dict:
        # dhu
        x = a["x"]
    elif type(a) == list:
        x = a[0]
    elif type(a) == set:
        x = a.to_dict()
    elif type(a) == tuple:
        x = a[0]
    else:
        return False
    if x not in a:
        return False
    return True
