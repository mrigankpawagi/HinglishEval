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
    n = int(n)
    if n < 1:
        return 1
    factorial = int((n - 1) / 2)
    # print("factorial: " + str(factorial))
    # print("n is " + str(n))
    start = 1
    factorial = factorial - 1
    # print(f(n) + " " + str(factorial))
    n = n - start
    factorial = factorial + 1
    # print("factorial: " + str(factorial))
    if f(n) != 1:
        factorial = factorial - 1
        n = n - start
    factorial = factorial + 1
    # print("factorial: " + str(factorial))
    ki = int(n / factorial)
    n = n % factorial
    # print("ki: " + str(ki))
    hota = factorial * ki
    hua = start
    # print("ki: " + str(ki) + " hua: " + str(hua) + " hota: " + str(hota) + " aki: " + str(hua
