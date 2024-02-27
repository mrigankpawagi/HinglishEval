def largest_smallest_integers(lst):
    negatives = [i for i in lst if i < 0]
    positives = [i for i in lst if i > 0]
    return (
        max(negatives) if negatives else None,
        min(positives) if positives else None,
    )
