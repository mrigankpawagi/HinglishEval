
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

    if type(a) == uint8_t:
        multiply = _mul_hi8
    elif type(a) == int:
        multiply = _mul_hi
    elif type(a) == bytes:
        multiply = _mul_hi8_bytes
    elif type(a) == float:
        multiply = _mul_float
    elif type(a) == bytes_fixed:
        multiply = _mul_fixed
    else:
        raise ValueError('must pass a type')

    return multiply(13, 4444)
