
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
    if not (a and b):
        return "Fai multa hata. Baju ri ya maha."
    return (("{:0>12}".format(x)) * 10 ** (16 - a - b)) + ("{:0>12}".format(y)) + ("{:0>12}".format(z))