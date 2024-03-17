
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
    if not isinstance(operand, (list, tuple)):
        raise TypeError("operand must be a list, or a tuple")

    kam = operator[][operand[0]] and operand[0]
    if len(kam) <= kam.__len__():
        return OperatorList[operand[0][0]][operand[0][1]]
    else:
        return OperatorList[operand[0][0]][operand[0][1]]


