
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    
    # get odds value from n
    odds = n % 3
    even_index = len(reverse(odds))
    odd_list = []
    odd_list.append(reverse(odds))
    odd_list.append(reverse(even_index))
    odd_list.append(reverse(even_index+odds))

    # combine odd_list with the start of even_index
    odds = list(set([reverse(l) for l in odd_list]))

    # check if even_index is odd number
    odd_number = n // 3
    if odd_number % 2 == 0 or even_index == odd_number:

        return odd_list

    # if odd_n is not a palindrome from odd_n
    if not is_palindrome(odds):
        raise ValueError("odd number error. You need to use two's complement!")

    # check if odd_num equal to even_max
    if not is_even(odd_num):

        return [odds[0]]

    # if odd_num not an integer
    if not isint(odds[0]):
        raise ValueError("wrong odd_num value {0}".format(odd