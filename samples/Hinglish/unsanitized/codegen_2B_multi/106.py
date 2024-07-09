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

    y = []
    for i in range(n):
        fact = 1
        y.append(fact)
        for j in range(1, i + 1):
            fact = fact * i
            y.append(fact)

    return y


# f(5) == [1, 2, 6, 24, 15]
# f(2) == [1, 1, 2]
# f(3) == [1, 2, 6]
# f(4) == [1, 4, 24]
# f(5) == [1, 8, 120]
# f(6) == [2, 6, 120]
# f(7) == [6, 120, 720]
# f(8) == [120, 720, 10080]
# f(9) == [120, 1440, 10080]
# f(10) == [243, 9840, 10080]
# f(11) == [4784, 2419200, 10080]
# f(12) == [204748, 40603520, 10080]
# f(13) == [7883941, 3237181400, 10080]
# f(14) == [6024447800, 24141869650000, 10080]
# f(15) ==  [34694027751770, 5473715646438700, 10080]
# f(16) ==  [1, 3, 10, 81, 5040, 10395, 966
