
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
    # Write your code here.
    #operand2 = []
    #operator2 = []
    #for i in range(len(operator)):
    #    operand2.append(int(operand[i]))
    #    operator2.append(int(operator[i]))

    # while len(operand2)!= len(operator2):
    #    for i in range(len(operand2)):
    #        if operand2[i] == operand2[i]:
    #            operand2.remove(operand2[i])
    #    if len(operand2)!= 0:
    #       operand2.append(int(operand[i]))
    #    else:
    #       operand2.append(int(operand[i]))
    #return sum([int(j) for j in operand2])
    if len(operand)!= len(operator):
        expression = ''
        operand2 = [operand[i] for i in range(len(operand))]
        operator2 = [operator[i] for i in range(len(operator))]
        while len(operand2)!= len(