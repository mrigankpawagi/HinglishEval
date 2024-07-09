
def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    if end1 - start1 <=0 and end2 - start2 <=0:
        return "NO"
    intersection = max(start1, start2)
    if start1 <= start2 <= end1 < end2:
        print(start1, end2)
        print(end1, end2 )
        return  "YES"
    elif start2 <= start1< end2 and end2 < end2:
        print(start1, end2 )
        print(start2, end2 )
        return  "YES"
    elif start1 < end2 and start2 < end1:
        return "YES"
    elif start1 <=start2 <= end1 < end2:
        return "YES"
    elif start1 <= start2 and end2 < end1:
        return "YES"
    elif start1 <= start2 <= end2 and end1 > end2:
        return "YES"

