

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    
    def sort_third(l: list):
        """Returns a list l[:] in which third items of l
        have been sorted. The third items are the ones that
        are not divisible by three."""
        third_items = [value for value in l if value % 3!= 0]
        def sort_third(l: list):
            """Returns a list l[:] in which third items of l
            have been sorted. The third items are the ones that
            are not divisible by three."""
            third_items = sorted([value for value in l if value % 3!= 0])
            return third_items
        return l[:]
    return sort_third(l)



#########################################
# Find the nth_to_last_element
#########################################

