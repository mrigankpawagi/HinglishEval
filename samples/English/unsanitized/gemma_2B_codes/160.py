
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    
    result = 0
    operand = operand + 1 

    # add operand 1 + operand 2, and keep repeating until length of operand and operator equals
    # result = operator + operand + result = operator + operand + operator + result
    for i in range(len(operator)):
        operand = operand + 1
        result = (operator[i] + operand)

    res = result // operand[0]
    return res


assert do_algebra(dict(operator='+', operand=[2, 3, 4, 5]), [0, 0, 0, 0]) == 9
assert do_algebra(dict(operator='-', operand=[2, 3, 4, 5]), [0, 0, 0, 0]) == 9
assert do_algebra(dict(operator='*', operand= [2, 3, 4, 5]), [0, 0, 0, 0]) == 24
assert do_algebra(dict(operator='*', operand = [2, 3, 4, 5, 6]), [0, 0, 0, 0]) == 10
# assert do_algebra(dict(operator='**', operand = [2, 3, 4, 5, 6]), [0, 0, 0, 0]) == 14
# assert do_algebra(dict(operator='/', operand = [2, 3, 4, 5, 6]), [0, 0, 0, 0]) == 48


def is_balanced(exp, depth=0):
    """
    Given one string expression.
    This function checks whether the bracket match.

    Example:
    is_balanced('()', '()')

    Return: boolean

    Complexity:
    Time   O(n**4)
    Space  O(n**4)

    """
    if not exp:
        return exp

    if '(' in exp:
        bracket_type = '('
        parenthesis = True
    elif ')' in exp:
        bracket_type = ')'
        parenthesis = True
    elif '[' in exp:
        bracket_type = '['
        parenthesis = False
    elif ']' in exp:
