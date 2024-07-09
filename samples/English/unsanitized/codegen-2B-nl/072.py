
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    def fl_object(q):
        '''
        Return True if the object q (q[::-1]) will fly, and False otherwise.
        
        Example:
        fl_object([3, 2, 3]) ➞ False
        # 2+3 is more than the maximum possible weight, but it's unbalanced.
        '''
        if len(q) < 1 or len(q) > self.max:
            return False
        return len(q) == 1 and sum(q) <= self.max

# ------------------------------------------------------------------------------

# a list that holds the values that will be tested for being the largest in a list
_largest_items_cache = {}

# helper function for computing the maximum of two integers (or floats) in Python
