

def sum_squares(lst):
    """
    Aapko ek numbers ki list di gayi hai.
    Aapko di gayi list ke squared numbers ka sum return karna hai,
    pehle har element ko list mein upper int(Ceiling) par round karo.
    Udaharan:
    Agar lst = [1,2,3] hai to output hona chahiye 14
    Agar lst = [1,4,9] hai to output hona chahiye 98
    Agar lst = [1,3,5,7] hai to output hona chahiye 84
    Agar lst = [1.4,4.2,0] hai to output hona chahiye 29
    Agar lst = [-2.4,1,1] hai to output hona chahiye 6
    """
    for i in range(0,len(lst)):
        tmp = sorted(list((str(k) for k in lst), sort=()))
        a=0
        for v in tmp:
            tmp[a]+=v*2
            a=-a
            if '+' not in tmp[a]:
                tmp[a]=1
    return(sum_squares((a))

