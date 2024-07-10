
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    return min(lst[1:], key=lambda x: lst[lst.index(x)])

if __name__ == '__main__':
    def test(input, expected):
        actual = next_smallest(input)
        message = '{} returned {}, expected {}'.format(
            type(input), actual, expected
        )
        assert expected is actual, message
    
    test([1, 5, 7, 4, 2], 2)
    test([5, 9, 7, 4, 1], 6)
    test([], None)
    test([1, 1], None)
    
    test([1, 2, 1, 3, 4], 1)
    test([1, 3, 4, 2, 3], 2)


# Your Code Below
