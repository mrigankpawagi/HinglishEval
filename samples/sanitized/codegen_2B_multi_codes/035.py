

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """    def find_max(first_element: int, remaining_elements: list, index: int):
        if remaining_elements[index] > first_element:
            return first_element
        if remaining_elements[index] == first_element:
            return find_max(first_element, remaining_elements, index + 1)
        else:
            return remaining_elements[index]

    return find_max(l[0], l[1:], 0)

