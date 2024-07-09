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
    # return karne ko numbers ko size ko parameter ke role hai
    if n < 2:
        return [1]
    # return karne ko numbers ko size ko parameter ke role hai
    if n <= 1:
        return [1]
    def fib(_min, _max):
        """
        f(4) == 1, f(5) == 1, f(6) == 2, f(7) == 29, f(8) == 58, f(9) == 89, f(10) == 144, f(11) == 230
        """
        if _min == _max:
            return 1
        result = [0]
        last = [0]
        i = 1
        while i < _min:
            result.append(last[i - 1])
            i += 1
        while i <= _max:
            tmp = 0
            if i == 2:
                tmp = 1
            elif i % 2 == 0:
                tmp = fib(i - 2, i)
            else:
                tmp = fib(i - 1, i) + fib(i - 3, i)
            result.append(tmp)
            i += 1
        return result
    # function ko return kart ko array ko list hai
    return fib(n - 1, n - 1)