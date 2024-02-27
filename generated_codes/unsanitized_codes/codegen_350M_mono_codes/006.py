from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parsed_input = paren_string.split('(')
    parsed_input = {int(i): j for i, j in parsed_input}
    return [parsed_input.pop(i) for i in sorted(parsed_input, reverse=True)]


class Sum(object):
    def __init__(self, sum_str: str, pre_sum: List[object]) -> None:
        self.pre_sum = pre_sum
        self.sum_value = int(sum_str)

    def get_sum(self) -> int:
        return self.sum_value + sum(self.pre_sum)

    def set_sum(self, new_sum_str: str) -> None:
        self.sum_value = int(new_sum_str)

    def __eq__(self, other):
        return isinstance(other, Sum) and self.sum_value == other.sum_value \
               and self.pre_sum == other.pre_sum

    def __gte_or_eq__(self, other):
        return isinstance(other, Sum) and self.sum_value >= other.sum_value


class TreeNode:
    """
    [4] in the sum subtree = true, there is a sum in the sum subtree of a pair of integers [sum_n],
    the sum of the given sum_n is lesser than the given sum_n.
    Given a sum_n, sum_{b, n-