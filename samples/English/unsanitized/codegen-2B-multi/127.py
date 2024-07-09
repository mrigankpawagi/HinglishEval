
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
    s_val = str(interval1[0])
    e_val = str(interval2[1])
    s_inter = interval1[0]
    e_inter = interval2[1]
    if s_inter == 0 or e_inter == 0 or s_inter > e_inter:
        return "NO"
    if s_inter <= e_inter:
        return "YES"
    if len(str(interval1[1] - interval1[0])) < 3 or len(str(interval2[1] - interval2[0])) < 3:
        return "YES"

    def sub_inter(val_a, val_b):
        val_c = min(val_a, val_b)
        val_d = max(val_a, val_b)
        return val_c, val_d

    inter_num = 0
    str_b = ""
    for i in range(2, len(s_inter)):
        srt = s_val[-i