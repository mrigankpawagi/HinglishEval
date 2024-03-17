
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
    operator_list = operator['+', '*', '-']
    # Operand list me kam kyuki same length hai, aur operator list me kam kyuki same length hai, means operator list me kyuki ek operator hota hai.
    operator_list_len = len(operator_list)
    operand_list = operand['+', '*', '-']
    operand_list_len = len(operand_list)
    index = 0
    # index ki value zero honge, operator list me kam se kam do operands hote hain.
    # operand_result = operand_list[0] + operator_list[0]['+'] + operand_list[1]

    if (operand_list_len and operator_list_len == 1):
        for i in range(operand_list_len):
            operator_result = {}
            operator_result['+'] = operand_list[i]
            sub_expr = do_algebra(operator_list[