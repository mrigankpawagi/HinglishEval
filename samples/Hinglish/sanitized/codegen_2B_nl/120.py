
def maximum(arr, k):
    """
    Ek array arr diya gaya hai integers ka aur ek positive integer k, return karo ek sorted list 
    lambai k ki maximum k numbers ke saath arr mein.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. Array ki lambai range mein hogi [1, 1000].
        2. Array ke elements range mein honge [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    
    assert(0 <= k <= len(arr)),'maximum input : %d' % (k,)       
    
    def sortedList(arr, k):
        if k == 0:
            return [],
        elif k == 1:
            return [1, 0],
        elif k == -1:
            return [arr[0], arr[-1]],
        
        assert(1 <= k <= len(arr)),'maximum input : %d' % (k,)
        arrLen = len(arr)
        if k < 0:
          