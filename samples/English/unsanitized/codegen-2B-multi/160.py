
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
    # Step 1: The first list has basic algebra operations
    s_operand = operator[0]
    s_operator = operator[1]

    # Step 2: The second list has operand
    n_operand = operand[0]
    i_operand = operand[1]

    # Step 3: If operator is not supported, just exit
    if s_operator not in operators + [c for c in str] + ['*', '/']:
        return "Unsupported Operator"
    while s_operator!= '+':
        if s_operator == '+':
            i_operand = operand[1] if n_operand!= 0 else 1
            operand.pop(1)
            n_operand = operand.pop(0)
        elif s_operator == '-':
            i_operand = 1 - i_operand
        elif s_operator == '*':
            i_operand = n_operand * i_operand
            n_operand = operand.pop(0)
        else:  # s_operator == '/'
            # Division:
            # If dividend is divided by zero, return zero.
            if n_operand