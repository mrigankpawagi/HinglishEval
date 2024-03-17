def largest_smallest_integers(lst):
    negative_integers = [num for num in lst if num < 0]
    positive_integers = [num for num in lst if num > 0]
    if negative_integers:
        max_negative = max(negative_integers)
    else:
        max_negative = None
    if positive_integers:
        min_positive = min(positive_integers)
    else:
        min_positive = None
    return (max_negative, min_positive)
