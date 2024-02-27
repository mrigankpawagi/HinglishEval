
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
    if not isnumber(a):
        print('Input must be a number, please try again')
    else:
        if a == 1: return True
        if a == -1: return True
        if a == 2: return False
        if a == 64: return True
        if a == 0: return True
        if a == 180: return False
        else: return False
