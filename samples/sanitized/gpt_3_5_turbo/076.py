def is_simple_power(x, n):
    if x == n ** int(x ** (1 / n)):
        return True
    else:
        return False
