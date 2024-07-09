
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    prod_list = []
    for i in arr:
        prod_list.append(abs(i) * product_sign(i))

    return sum(prod_list)

Note your method is already pretty close to what your example is asking for as the answer is the sign of the sum, but your answer only works with positive inputs. The example also assumes that for a given array, your for loop only counts how many of each sign you have in a given array e.g. if you have two elements a, b, a will give you -2, b, -2 giving you a final result of 1. 
Another note regarding your use of abs, what you are doing is calculating the absolute value of each element that you multiply with product_sign. If you want to do the same as in the example you provided with a list of signs, you are just going to have to keep in mind that the product_sign function returns 1 if it's a sign of 1, -1 if it's a sign of -1, and 0 if it's a sign of 0.

