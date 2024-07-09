
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    idx = min(0, len(arr) - 1)
    can_arrange = arr[:idx] + 1
    for i in reversed(idx + 1, idx + arr.count()):
        can_arrange = max(0, arr.count()-i) + 1

    return can_arrange

print "\nCannot arrange: [" + str(can_arrange([[1,2,3,4,5]])) + "]\n"
print "\nCannot arrange: [" + str(can_arrange([1,2,3])) + "]\n"
print "\nCannot arrange: [" + str(can_arrange([1,2,3,4,5])) + "]\n"

print "\nCannot rearrange: [" + str(can_arrange([2,2,3,4,5])) + "]\n"
print "\nCannot rearrange: [" + str(can_arrange([1,2,3])) + "]\n"
print "\nCannot rearrange: [" + str(can_arrange([1,2,3,4,5])) + "]\n"

A:

