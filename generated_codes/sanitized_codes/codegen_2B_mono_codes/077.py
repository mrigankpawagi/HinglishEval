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
    if a == "":
        return True
    if a.isnumeric() == True:
        a = int(a)
        if a % 3 == 0 and a % 4 == 0 and a % 7 == 0:
            return print(True)
        else:
            return print(False)