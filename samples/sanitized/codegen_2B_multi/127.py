
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
    return (interval1[0], interval1[1]) == (interval1[0], interval2[1]) or \
            (interval1[0], interval1[1]) == (interval2[0], interval1[1]) or \
            (interval1[0], interval1[1]) == (interval2[0], interval2[1]) or \
            (interval1[0], interval1[1]) == (interval1[0]+2, interval1[1]-2) or \
            (interval1[0], interval1[1]) == (interval1[0]-2, interval1[1]+2) or \
            (interval2