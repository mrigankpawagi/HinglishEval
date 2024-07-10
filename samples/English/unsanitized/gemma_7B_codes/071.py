
def triangle_area(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar teeno sides ek valid trikon banate hain to trikon ka area 2 decimal points tak round off karke return karo.
    Anyatha -1 return karo.
    Teen sides tabhi ek valid trikon banati hain jab kisi bhi do sides ka yog teesri side se adhik hota hai.
    Udaharan:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    if sum(a,b,c) < 3:
        answer = -1
    else:
        answer = (a * b) / 2
    return round(answer, 2)


def maximum_subsequence_sum(a, b, c, d):
    """
    Teeno numbers positive number hain. Ek random integer x choose kar lo. Aise karke sum of x with a, b, c, d ki maximum hai?
    a, b, c, d se ek side jaan liye jisse result maximum ban sake.
    """


def longest_monotonic_subsequence(a, b, c):
    """
    Teeno sequences 1 se 5 tak ka hain. Ek string (S1 S2 S3... Sn) print karo kahke jabki vo monotonically increasing sequence ho jo maximum kaam se kaam subse sequence banta hain.
    """


def count_triangles_in_array(a):
    """
    Eky integer array ka use karke jo minimum amount of triangles possible hain (kisi side ka value maximum 10 000 pe ho).
    """


def can_sum(target, array):
    """
    Ek integer target (5) diya gaya hain aur ek array of non-negative numbers (7 1 5 3 3 9). Kuch integer number 5 banaye jaye?
    """


def can_construct(target, arr):
    """
    Can_sum ka variant. Ek integer target (10) diya gaya hain aur ek array of non-negative numbers (1 2 3 4 5). Kuch way find karo target ko achieve karo. Kuch number array ko add karke.
    """


def unique_number_in_stream(array):
    """
    Stream of non-negative numbers diya gaya hain. Kuch numbers ek array mein store kiye jo dekhate hain. Ek integer aise choose karne ka try karo jo ki array ko duplicate nhe ho, ya ki duplicate ho.
    """
