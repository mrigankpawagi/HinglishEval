
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
    if not a:
        return False
    m = a*m
    if isint(m) and m % pow(3, a-1) == 0:
        return True
    elif isint(a) and 3*a==len(str(a)):
        return True
    else:
        return False

f = open('in','r')
for tmpt in f:
    num=tmpt.strip('\n')
    print(iscube(int(num)))
# End of code