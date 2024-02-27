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
    # multiply() is a function and not a method.
    # So, you have to give the method for the arguments
    # as parameters.
    # I think that we're dealing with a list in here
    a = a.split(", ")
    b = b.split(", ")
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    result = a[0] * b[1] + b[0] * a[1]
    return result