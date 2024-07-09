
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
    l = [1, 2, 4, 8, 16]
    index = 0
    s = 1
    for i in range(1, n):
        if i % 2 == 0:
            s *= l[index]
            index += 1
    return s


