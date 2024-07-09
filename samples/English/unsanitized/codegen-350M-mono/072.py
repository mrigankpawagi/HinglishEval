
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
    q = list(q)
    nq = len(q)
    tq = q[:nq//2]
    tw = q[nq//2:]
    nmax = max(tw)
    nmaxnq = len(tw)
    if nq == nmax:
        return False
    a_sum = q[0] + q[1] + q[nq//2] + sum(q[nq//2:])
    if nmaxnq == nq and tw[0] < a_sum:
        return False
    b_sum = tw[0] + tw[-1] + sum(tw[1:])
    if tw[0] < b_sum:
        return False
    c_sum = tw[0] + tw[-1] + sum(tw[1:nq//2])
    if tw[-1] < c_sum:
        return False
    d_sum = tw[-1] + a_sum + sum(tq)
    if tw[-1] < d_sum:
        return False
    return True

# Driver Function
#
# # Prints whether the test will pass or