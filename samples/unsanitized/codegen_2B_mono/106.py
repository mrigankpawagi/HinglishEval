
def f(n):
    """
    Function f ko implement karo jo n ko parameter ke roop mein leta hai,
    aur ek list return karta hai jiska size n hota hai, aisa ki index i par element ka value i ka factorial hota hai agar i even hai
    ya fir 1 se lekar i tak ke numbers ka sum hota hai otherwise.
    i ka start 1 se hota hai.
    i ka factorial 1 se lekar i tak ke numbers ka multiplication hota hai (1 * 2 *... * i).
    Udaharan:
    f(5) == [1, 2, 6, 24, 15]
    """
    k = [i for i in range(n)]
    k1 = [x for x in range(1)]
    for i in range(2,n+1):
        k1.append(i*k1[-1])
    # print(k1)
    i=k.index(1)
    k_c = k.copy()
    # print(k,k1)
    k_c[i] = k1[i]
    k_c.insert(0,k1[i])
    k_c.append(k1[i])
    # print(k1,k,k_c)
    return k_c


