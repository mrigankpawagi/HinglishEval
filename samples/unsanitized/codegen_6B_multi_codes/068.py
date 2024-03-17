
def pluck(arr):
    """
    "Ek array diya gaya hai jo ek tree ki branch ko represent karta hai jisme non-negative integer nodes hote hain
    aapka task hai ek node ko pluck karke return karna.
    Plucked node woh hona chahiye jiska sabse chhota even value ho.
    Agar multiple nodes milte hain jinka same sabse chhota even value ho toh woh node return karo jiska sabse chhota index ho.

    Plucked node ko ek list me return karna chahiye, [ sabse_chhota_value, uska index ],
    Agar koi bhi even values na ho ya diya gaya array khali ho, toh [] return karo.

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 ka sabse chhota even value hai, aur 2 ka sabse chhota index hai.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 ka sabse chhota even value hai, aur 2 ka sabse chhota index hai. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 sabse chhota value hai, lekin yahan do zeros hain,
                     isliye hum pehla zero choose karenge, jiska sabse chhota index hai.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    
    # Solution starts here
    
    if arr == []:
        return []
    
    n = len(arr)
    
    # Check if it is even number
    if n % 2!= 0:
        raise Exception('Node count value must be a number even, as it takes 2 values')
    
    # This is the way to handle