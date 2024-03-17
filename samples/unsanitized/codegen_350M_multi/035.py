

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) < 2:
        return 0
    low_pos = -1
    high_pos = -1
    result = low_pos
    for j in range(len(l)):
        if l[j] < low_pos + 1:
            low_pos = j
        elif l[j] == low_pos + 1:
            if (not [low_pos, low_pos + 1] in oplist) and \
                    (not [high_pos, high_pos + 1] in oplist):
                high_pos = j
        else:
            if (low_pos, low_pos + 1) in oplist:
                if not [high_pos, high_pos + 1] in oplist:  # no next element
                    low_pos = high_pos = j
                    result = low_pos
                else:
                    result = high_pos
    return result

with open(sys.argv[1], 'r') as f:
    for line in f:
        key, value = line.strip().split()
        obj = {key: value}
        if not key.startswith('#'):
            if key not in oplist:
                oplist[key] = []
            oplist[key].append(obj)
print(sum( [max_element(item) for item in oplist.values()] ))
