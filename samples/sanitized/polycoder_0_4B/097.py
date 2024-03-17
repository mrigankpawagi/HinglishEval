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
    if len(a) != len(b):
        raise ValueError(f"len(a) and len(b) should be same length!")
    return numpy_digit_sum(a)[0] * numpy_digit_sum(b)[0]
