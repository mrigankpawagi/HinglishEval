
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


def get_root(branch_array):
    return branch_array if branch_array != -1 else None


def root(node_id, branch_array):
    if branch_array is None:
        return None
    left = branch_array[2 * node_id + 1]
    right = branch_array[2 * node_id + 2]
    root_node = get_root(branch_array[node_id])
    return root_node, root_id_right(right), root_id_left(left)


def root_id_left(node):
    return None

def root_id_right(node):
    return None



class Solution(object):
    def pluck(self, branch_array):
        if len(branch_array) == 0:
            return []
        if branch_array is None:
            return None
        min_even_node = min(
            branch_array, key=lambda x: x if x % 2 == 0 else float('inf'))
        if min_even_node == float('inf'):
            return []
        min_even_idx = branch_array.index(min_even_node)
        min_even_node_and_id = [
            min_even_node, min_even_idx]
        return min_even_node_and_id

# Driver Code:
if __name__ == "__main__":
    branch = [4, 2, 3]
    print Solution().pluck([4, 2, 3])
    
    # [2,1]
