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
    if len(operator) == 1:  # if any one operand
        ka_list = operator
    else:
        ka_list = operator[: len(operand)]
        for o in operand:
            ka_list = operator[: len(o)]
        ka_list = operator[len(operand) :]
    result = eval(operator)
    for i in xrange(len(operator)):
        if operator[i] != "+":
            result *= operand[i]
    return result