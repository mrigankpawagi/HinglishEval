
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
    # TODO - do lists diye gaye hain, operator aur operand.
    # pehla list basic algebra operations ka hai, aur dusra list integers ka hai. Diye gaye do lists ka use karke algebraic 
    # expression banaye aur is expression ka evaluation return kare.
    #
    # Basic algebra operations:
    # Addition ( + ) 
    # Subtraction ( - ) 
    # Multiplication ( * ) 
    # Floor division ( // ) 
    # Exponentiation ( ** ) 

    ar = [2, 3, 4, 5]
    # operator['+', '*', '-']
    # ar = [2, 3, 4, 5]

    # pehla operator list ki length operand list ki length se ek kam hoti hai.
    if len(operator) == 2 and len(operand) == 2: # operator + 2
        # operator['+', '*', '-'] ka list ki length 2 pehli hota hai, aur oper