
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
    total = 0.0

    for index in xrange(len(operator) - 1):
        # get value of operator[index]
        value = 0
        if index == len(operator) - 1:
            # first operand
            index = 0
        if index in operand[0]:
            # second operand
            index += 1
        value = float(operand[index]) * operator[index]
        total += value

    return total


# calculate the probability that the random value in [0, 1, 2]
# given by operator[index]: 
_calculate = 0
_maximum_value = 1.0
