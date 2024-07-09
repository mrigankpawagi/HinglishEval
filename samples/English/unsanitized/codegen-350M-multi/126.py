
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    def is_sorted_helper(seq):
        seen = set()
        for item in seq:
            if item not in seen:
                seen.add(item)
                if item not in seen:
                    return False
        return True
    return is_sorted_helper(lst)

if __name__ == '__main__':
    print(is_sorted([100, 20, 37, 10, 21]))
    print(is_sorted([100, 9, 20, 37, 10]))
    print(is_sorted([1, 10, 37, 20, 9]))
    print(is_sorted([-1])-1)
    print(is_sorted([-1, 1, 20, 37, 10]))
    print(is_sorted([3, 5, 9, 9, -1])-1)
    print(is_sorted([-1, 12, -5, 9, -2, 8, 15, -18, -10])-1)