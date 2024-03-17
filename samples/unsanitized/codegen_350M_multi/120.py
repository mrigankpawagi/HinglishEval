
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

    # create nk element hash list nk for each element
    hash_arr = defaultdict(set)

    # make a dummy nk element list
    nk_list = [0] * len(arr)

    for a in arr:
        hash_arr[a].add(k)
        nk_list[k] = a

    # initialize nk element list by creating nk elements
    nk_list = list(range(len(arr)))

    # make nk elements out of nk element list and nk of nk list
    nk_ele_list = nk_list[:]

    # make sure that k is sorted in the last case
    k_array = nk_list[nk_list.index(nk_list.pop(0))]
    k = k_array
    
    if len(nk_list) > 0:
        
        arr_list_copy = nk_array.copy()
        
        for a in nk_list[:]:
            arr_list_copy.remove(arr_list_copy[a])

    if k < nk_ele_list.index(k_array):
        
        for i in nk_ele_list:
            nk_list[i] = n