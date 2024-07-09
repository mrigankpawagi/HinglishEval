
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
    operand = ''.join([operator[i] for i in operator_list[-1]])
    algebra = operator_list[0][2] - 1
    if len(operand) == 1:
        operators = operator[1:]
        algebras = [1]

    def algebric_operator(operator, operand):
        if len(operand) == 1:
            operator_list = operand
            operator = operator_list[0]
        elif operator[2] == 1:
            operand_list = operator[2]
            operator = operand[1]
        elif len(operand_