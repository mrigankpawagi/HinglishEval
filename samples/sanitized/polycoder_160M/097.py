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
    if a != b:
        return a * b**2 + 128 * a + b
    while not a == 0:
        a = b * (1 + int(b))
        b *= 2**23
        if a != b:
            return a * b**2 + 128 * a + b
    return a * b**2 + 128 * a
