

def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    k1, k2 = l1, l2
    new_elements = []
    sorted_k2 = {k1: k2[0]}

    # Make sure k2 (and k1) do not have duplicates or be in lists.
    new_elements = [k.data.index(k2) for k in sorted(l2)]

    # Sort by element.
    sorted_k2.sort(key=operator.attrgetter('element_k2_index', lambda el: el[1]))

    # Check if list contains element.
    if len(new_elements) == 1:
        # Recurse.
        k1, new_k2 = sorted_k2[k1, new_elements[0]], sorted_k2[k2[0], new_k2]
    else:
        # Expand list by element.
        k1_el, new_k1_el = new_elements
        new_elements.append(k1_el)
        new_k1_el = sorted_k1[k1_el, new_elements[0]]

    # Sort by unique integer element.
    element_k2_index = operator.attrgetter('element_k2_index', lambda el: el[1][0])
    if element_k2_index[0] is not None:\
        k2_index = element_k2_index