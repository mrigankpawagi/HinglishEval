def is_simple_power(x, n):
    if n == 1:
        return x == 1
    power = 0
    while n ** power < x:
        power += 1
    return n ** power == x