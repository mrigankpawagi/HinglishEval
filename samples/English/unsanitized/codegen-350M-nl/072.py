
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
    def max_weight(q,w):
        '''
        Return the maximum weight of all palindromic palindromic lists contained in the dictionary defined by q, and w.

        Defining the max_weight function requires two parameters: q and w. (q needs to have a key containing the name of the list).
        q is a dict containing all lists contained in the dictionary, and w is a tuple of the types of the list elements.

        We need to convert the list q into a dict and the tuple w into a tuple of types. Otherwise the function will return False.
        

        @staticmethod
        def max_weight(q,w):
            '''
            Return the maximum weight of all palindromic palindromic lists. The tuple containing the maximum weight for each list is