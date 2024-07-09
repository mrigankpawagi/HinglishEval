def compare_one(a, b):
    a1 = float(str(a).replace(',', '.'))
    b1 = float(str(b).replace(',', '.'))
    if a1 > b1:
        return a
    elif a1 < b1:
        return b
    else:
        return None