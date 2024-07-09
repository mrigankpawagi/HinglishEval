

def sort_third(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' wahi hai jaisa l hai un indices par jo three se divisible nahi hote, jabki uske values un indices par jo three se divisible hote hain, wahi hoti hain
    jaisi corresponding indices ki values l ki hoti hain, lekin sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    k=0
    l.sort(reverse=True)
    k +=1
    for i in range(k):
        # print(l[i])
        j=i+2
        for j in range(i,len(l)):
            if l[i]%3==0 and l[j]%3==0 and sorted(l[i:j])==sorted(l[i:j]):
                l[i:j]=sorted(l[i:j])
    



        



    """ function sort_third(l: list)
        >>> sort_third([])
        []
        >>> sort_third([7,2,3,4])
        [2, 3, 4, 7]
    """
