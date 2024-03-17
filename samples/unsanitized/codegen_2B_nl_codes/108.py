
def count_nums(arr):
    """
    Ek function likho count_nums jo ek array of integers leta hai aur return karta hai
    un elements ki sankhya jinka digits ka sum > 0 hota hai.
    Agar koi number negative hai, to uska pehla signed digit negative hoga:
    jaise ki -123 ke signed digits hote hai -1, 2, aur 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    pos = 0
    while pos < len(arr):
        if (arr[pos])!= 0:
            pos += 1
        else:
            count_nums(arr)
    return len(arr)

A:

Python is not object-oriented as it doesn't have an in-place operator, so you will need to return the array in the first place. Also, since count_nums takes a variable of the type type(np.array) (the type of the object returned by numpy.array), you need to pass it a list of ints to count, not an array with ints:
>>> arr = np.array(['0123', '123456789', 0], dtype=int)
>>> [1 for x in xrange(10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> count_nums(arr)
9

You would be better to write your own, in-place, version of the Count-1-Less-than-sign operation:
