
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    if z == 0: return False
    return abs(x) == sum(map(int, [y, z]))


class Solution(object):
    def is_balanced_binary_tree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        if root.left is None and root.right is None:
            return True
        elif root.left is None:
            return is_balanced_binary_tree(root.right)
        elif root.right is None:
            return is_balanced_binary_tree(root.left)
        elif any_int(abs(root.left.val), abs(root.val), abs(root.right.val)) or \
                any_int(abs(root.val), abs(root.left.val), abs(root.right.val)):
            return is_balanced_binary_tree(root.left) and is_balanced_binary_tree(root.right)
        else:
            return False

