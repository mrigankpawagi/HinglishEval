
def do_algebra(operator, operand):
    """
    Do lists diye gaye hain, operator aur operand. Pehla list basic algebra operations ka hai, aur 
    dusra list integers ka hai. Diye gaye do lists ka use karke algebraic 
    expression banaye aur is expression ka evaluation return kare.

    Basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Udaharan:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Dhyan de:
        Operator list ki length operand list ki length se ek kam hoti hai.
        Operand ek non-negative integers ki list hoti hai.
        Operator list me kam se kam ek operator hota hai, aur operand list me kam se kam do operands hote hain.
    """
    if not operand:
        if not operator:
            raise ValueError("no operators provided")
        else:
            raise ValueError("operator is not set")
    else:
        if not isinstance(operator, list):
            raise TypeError("operator is not of list")
        if len(operator)!= 2 or not isinstance(operand, list):
            raise TypeError("operator is not of list operand expected: [%s]" % (str(operator)))

    if not (operator in OPERATORS_NAME_LIST + OPERATORS_LIST_ADD + OPERATORS_LIST_SUB + OPERATORS_LIST_MUL + OPERATORS_