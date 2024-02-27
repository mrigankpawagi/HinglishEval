def compare_one(a, b):
    if type(a) == type(b):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        b = b.replace(",", ".")
        if a > float(b):
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        a = a.replace(",", ".")
        if float(a) > b:
            return a
        else:
            return b
    else:
        return None
