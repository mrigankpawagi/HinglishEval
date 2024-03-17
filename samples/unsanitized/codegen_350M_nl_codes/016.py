

def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    s = string.split(string, "")
    j = next(s)
    while not j:
        j = next(s)
    for f in s[j]:
        j -= 1
        n, c = int(f.isdigit())
        j -= n - 1
        k = next(s)
        while j > 0 and k[0] in c or j < n and k[0]!= c or j < n and k[j]!= c or j < n and k[0]!= c:
            int(k)
    j = next(s)
    while j < len(s):
        j = next(s)
    return j

