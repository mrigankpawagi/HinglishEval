

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    opening_brackets = {">": ">", "<": "<"}
    close_brackets = {">": "<"}

    def is_correct(bracket):
        count = 0
        for closing_bracket in close_brackets:
            if bracket.startswith(closing_bracket):
                count += 1
        if count == len(close_brackets):
            return True
        else:
            return False


    new_brackets = []
    for bracket in brackets:
        if bracket not in closing_brackets:
            while bracket!= ")":
                new_brackets.append(bracket)
                bracket = close_brackets[bracket]
        else:

            new_brackets = new_brackets[:-1]
            if is_correct(bracket):
                new_brackets.append(bracket)
        bracket = close_brackets[bracket]

    return "".join(new_brackets) in brackets or "#" in brackets
class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = {">": "<", "<": ">"}

        stack = []
        for bracket in s:
            if bracket not in opening_brackets:
                stack.append(bracket)
            else:
                stack.pop()

                # if we get to the end of the brackets, it's a correct bracket
                # because all its brackets except the last one contain closing brackets
                if bracket == stack[-1]:
                    stack.pop()

        return len(stack) == 0

for bracket_type in [">", "<", ">="]:
    s = Solution()
    # TODO: change this code
    assert s.is