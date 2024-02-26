
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
    if len(operator) < 2:
        return result
    elif len(operator) == 2:
        result = calculate(operator[1], operand[0], operator[0])
    else:
        operator_idx = 1
        operand_idx = 0
        for operator_char, op_char, operand_char in zip(operator, operator[1:], operand):
            result = calculate(result, operand[operand_idx], operator_char)
            operand_idx += 1
            operator_idx += 1
            if operator_char == '-':
                result = calculate(result, -operand[operand_idx], '-' + operator_char)
    return result


