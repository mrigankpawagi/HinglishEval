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
    a = a % 10
    if (a % 10) == 1:
        yield "1"
    else:
        if a > 0:
            yield "17"
        elif a < 0:
            yield "12"
        else:
            yield "0"
        while a:
            yield "10"
            a -= 1
        if b:
            return "0"
        for k in xrange(0, 15):
            yield "%d" % k
