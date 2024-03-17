def will_it_fly(q, w):
    return sum(q) <= w and q == q[::-1]