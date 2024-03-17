
def multiply(a, b):
    """
    Do integers ka input lekar unke unit digits ka product return karega ye function.
    Maan lo ki input hamesha valid hoga.
    Udaharan:
    multiply(148, 412) ka return hoga 16.
    multiply(19, 28) ka return hoga 72.
    multiply(2020, 1851) ka return hoga 0.
    multiply(14,-15) ka return hoga 20.
    """
    if not isinstance(a, int):
        a = a.val
    if not isinstance(b, int):
        b = b.val
    if a <= 9 and b < 10:
        return a*b
    else:
        return multiply(a/10,b/10)


assert multiply([19,28,7,15,1],[10,7,1,22,5,19,14]) == 0

assert multiply([2,2],1) == 2
assert multiply([2,2,3],1) == 7

assert multiply([1,2],1) == 2
assert multiply([1,2,1],[1,2,2,3,4,1,0]) == 11

assert multiply([5,18],22) == 1
assert multiply([5,18,37],[14,19,10]) == 21

import math
assert multiply([30,60,30,210],14) == 1521

if __name__=='__main__':
    import doctest
    doctest.testmod()
