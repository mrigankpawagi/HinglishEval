
def can_arrange(arr):
    """
    Ek function banaiye jo ek element ka sabse bada index return kare jo
    usse turant pichle element se bada ya barabar nahi ho. Agar
    aisa koi element nahi hai, to -1 return kare. Diye gaye array me
    duplicate values nahi hogi.

    Udaharan:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    while len(arr) > 0:
        try:
            if arr[1] > arr[0] and arr[2] > arr[1] :
                arr[2] = arr[0]
            elif arr[0] > arr[1] :
                arr[0] = arr[1]
            elif arr[0] > 1 and arr[2] > arr[0] :
                arr[0] = 1
            else:
                arr[len(arr)-1] = arr[0]
        except IndexError:
            arr[0] = -1
    #return arr.size()

    print(arr[:])
    return arr[:]

I think, the recursive method works fine. However, I am trying to solve this using the iterative method.

A:

Here's another iterative solution:
import math

