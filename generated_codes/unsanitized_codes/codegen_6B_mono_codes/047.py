

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    if len(l) % 2 == 1:
        return sorted_l[len(l) // 2]
    else:
        return (sorted_l[len(l) // 2 - 1] + sorted_l[len(l) // 2]) / 2

assert median([34, 17, 21, 3, 5, 2]) == 3
assert median([-20, -12, 11, 13, -5]) == -5

## ================================ Stretch Goal ================================
## You want to implement the missing code,
## so that the lines of code actually do something.
## (no need to change the existing tests)

## Remember: the point of a Huffman Tree is to assign
## a binary number (or a string under your fancy) to a node,
## and then recursively assign a binary number (or a string)
## to all of its descendants.

##########################
## Task 7: Huffman Coding ##
##########################

# Do not use code from any other file.
# Write your own code here


class Node(object):

    def __init__(self, data, freq: int, left_child=None, right_child=None):
        self.data = data
        self.freq = freq
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return "Node object for data = {} and freq = {}".format(
            self.data, self.freq
        )

    def __eq__(self, other):
        return self.data == other.data and self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq


