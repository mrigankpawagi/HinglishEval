

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_element = {}
    for element in l:
        if element not in unique_element:
            unique_element[element] = 1
        else:
            unique_element[element] += 1

    return unique_element


if __name__ == "__main__":

    print("Sorting elements in a list gives following result:\n")
    print("\t", unique([3, 2, 1, 4]))
