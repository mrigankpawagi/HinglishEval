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
        return a * b
    else:
        return multiply(a / 10, b / 10)