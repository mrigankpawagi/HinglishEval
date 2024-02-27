

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return [k for k, g in groupby(l) if g == l.count(k)]

# Eksam før kun i gange korsok både år gange korten har ved åkka selv.
# print(find_longest_sequence('AAAAAACCCAAABBBDA'))