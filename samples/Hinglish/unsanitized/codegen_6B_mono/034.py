

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return r = []
    dic = {}
    for ele in l: #lista to hume element print kardo
        if ele not in dic: #eg:
            dic[ele] = 1
        else:dic[ele] += 1 #element exist ki count print karo

    for k,va in dic.items():
        if va == 1: #if va mein 1 hai
            r.append(k) #
    return r

#
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])