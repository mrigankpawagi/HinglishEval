
def sort_array(arr):
    """
    Is Kata mein, aapko ek array ko sort karna hai jo non-negative integers ka hoga, 
    binary representation mein ones ki sankhya ke hisaab se ascending order mein.
    Agar ones ki sankhya same ho, toh decimal value ke basis par sort karo.

    Isko aise implement karna hai:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    if type(arr) is not list:
        raise Exception("The type of input list need to equal to list type %s in %s or '%s'"
                         % (type(arr), "tuple", type(arr)))
    try:
        return arr[0]
    except IndexError:
        raise IndexError("Index for Kata is index in list of 0 to (%d) with type: %s" % (len(arr), type(arr)))

