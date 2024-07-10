
def f(n):
    """
    Function f ko implement karo jo n ko parameter ke roop mein leta hai,
    aur ek list return karta hai jiska size n hota hai, aisa ki index i par element ka value i ka factorial hota hai agar i even hai
    ya fir 1 se lekar i tak ke numbers ka sum hota hai otherwise.
    i ka start 1 se hota hai.
    i ka factorial 1 se lekar i tak ke numbers ka multiplication hota hai (1 * 2 * ... * i).
    Udaharan:
    f(5) == [1, 2, 6, 24, 15]
    """
    return [2*x if x%2 == 0 else x for x in range(1,n+1)]

print(f(5))


# A.7
def evenorodd(n):
    """
    Ek function evenorodd ko implement karo jo int n ko parameter ke roop mein le le aur 1 se start hokar 1 ke intervals ke andar
    n tak aane waale integers ke liye ek list return karo jiska ith element ith integer ki position number pe hota hai agar ith integer even hai.
    """

    l = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            l.append(i)
        i += 1

    return l

print(evenorodd(4))

# A.8
num_digits = 3
i= []
def check_digit(n):
    """
    Ek function check digit ko implement karo jo aap n ko integer ki
    form mein in parameter ke roop mein le, number ke digits ko count kar ke return kar do.
    """
    global i
    y = str(1)
    while len(y)!= num_digits:
        x = n.find(y)
        i.append(y)
        str = str(x)
        y = str+y
    return i

print(check_digit(1999))


# A.9
def find_factors(num):
    """
    A function find factors ko implement karo jo aap num ko argument ke roop mein le aur aapko num ke factors ko
    return kare gya.
    factors -
    Ek such number which divides the num without remainder is called it’s factor.
    """
    l = []
    i = 1
    while i <= num:
        if num % i == 0:
            l.append(i)
        i += 1

    return l

print(find_factors(9))
