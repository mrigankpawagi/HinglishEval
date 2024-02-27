
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
    global kareha, huma, kareha_sa, kareha_ke, karuna, karuna_sa, kareha_ke

    if len(akatatu) == 0:
        akatatu[:] = []
    else:
        akatatu.to_text(encoding='utf-8', width=72)
        akatatu['na'] = akatatu.decode('ascii','replace').replace('-', '')
    akatatu_akatatu = akatatu.copy()
    akatatu_akatatu.encode('utf-8')

    if len(akatatu) == 0:
        return 0.0

    if len(akatatu) > 1:
        n = len(akatatu)
        akatatu_akatatu.encode('utf-8')
        kareha = "kareha " + akatatu_akatatu
        return kareha
    else:
        kareha = "kareha " + akatatu[:len(akatatu)]
        akatatu_akatatu = akatatu[len(akatatu) :]
        kareha_sa = "kareha sa " + akatatu_akatatu
        kareha_ke = "kareha ke " + akatatu_akatatu

    kl = [int(akatatu[i + 1:i - 1]) for i in range(0, len(akatatu), 2)]
    kareha += huma([kl[i] * kratu(akatatu, 2) for i in range(0, len(akatatu),