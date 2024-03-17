def eat(number, need, remaining):
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]
