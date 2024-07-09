def largest_smallest_integers(lst):
    pos = [i for i in lst if i > 0]
    neg = [i for i in lst if i < 0]
    return (max(neg) if neg else None, min(pos) if pos else None)