
def intersection(interval1, interval2):
    """
    Aapko do intervals diye gaye hain,
    jahan har interval ek integers ki jodi hoti hai. Jaise ki, interval = (start, end) = (1, 2).
    Diye gaye intervals closed hote hain matlab ki interval (start, end)
    dono start aur end ko include karta hai.
    Har diye gaye interval ke liye, maan liya jata hai ki uska start uske end se kam ya barabar hota hai.
    Aapka task hai yeh determine karna ki in dono 
    intervals ke intersection ka length ek prime number hai ya nahi.
    Udaharan, intervals (1, 3), (2, 4) ka intersection (2, 3) hota hai
    jiska length 1 hota hai, jo ki ek prime number nahi hai.
    Agar intersection ka length ek prime number hai, to "YES" return karo,
    nahi to, "NO" return karo.
    Agar do intervals intersect nahi karte, to "NO" return karo.


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    try:
        start = min([min(i1, i2) for i1, i2 in interval1], max(i1, i2))
        interval1 = list(range(1, start + 1))

        end = start + max(map(min, interval1), default=min(interval1) + 1)
        # if karo
        if not end == interval1[0]:
            return end
        # endif
    except IndexError:
        return None

    try:
        start = min([min(i1, i2) for i1, i2 in interval2], max(i1, i2))
        end = start + max(map(min