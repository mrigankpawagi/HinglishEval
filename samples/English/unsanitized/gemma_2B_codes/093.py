
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
   
    message = list(message)
    
    for letter in range(len(message)):
        if message[letter] in ('a','e','o','u','i' ):
            message[letter] = message[letter] + 2;
            
        else:
            message[letter]= message[letter]+1
    result = "".join(map(str,message))
    
    return result

    
# your code
# import copy
# 
# for letter in range(len(message)):
#     if message[letter] in ('aeiouAEIOU'):
#         message[letter] = message[letter] + 2;
#     
#             message[letter]= message[letter]+1
# 
# 
# return result



# test 
if __name__ == '__main__':
    import doctest
    
    doctest.testmod()



filepath: 05_09_2017/06/02/15_sum_pairs.py

# Write a function to find all element pairs in an array whose sum = k (the sum should not exceed a given K). 
# There is a helper function available for this problem, it should take two inputs array and a K. The 
# array will be of integers, the function should return a list of such element pairs.

# Your job is to optimize the implementation to be better: the complexity should be linear without 
# using a 2D array and without sorting the array, and the overall time complexity should be less than 
#  O(n^2).

# Write some tests for this, make sure to handle the edge cases correctly.

from collections import defaultdict
from itertools import combinations
from collections import Counter


def sumOfK(arr, k):
    n = len(arr)
    if n == 0 or k < 0:
        return []
    result = []
    for comb in combinations(arr, 2):
        if comb[0] + comb[1] == k:
            result.append(comb)
    return result


# test 1
if __name__ == '__main__':

    # no duplicates
    arr_1 = [4, 4, 4, 4, 4]
    k = 6