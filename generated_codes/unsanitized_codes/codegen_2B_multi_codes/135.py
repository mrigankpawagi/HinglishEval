
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    assert len(arr) > 0
    arr = sorted(arr)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            print arr[i], arr[i + 1], arr[i + 2]
        else:
            return i
    return -1
  
if __name__ == "__main__":
    # Build a random test case
    arr = []
    for i in xrange(100):
        arr.append(random.randrange(100))
    arr = sorted(arr)
    # Create a decorator which will compute a value that can_arrange returns.
    # This should look similar to can_arrange.
    arr = unmodifiable_for_testing(arr, can_arrange)

    # Run the tests
    print can_arrange(arr)
    print can_arrange(-1)
    print can_arrange((1,2))