def eat(number, need, remaining):
    total_gajar = number + remaining
    if total_gajar >= need:
        eaten_gajar = need
        remaining_gajar = total_gajar - need
    else:
        eaten_gajar = total_gajar
        remaining_gajar = 0
    return [eaten_gajar, remaining_gajar]