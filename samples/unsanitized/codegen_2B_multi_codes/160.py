
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
    if operator is None or operand is None or len(operator)!= len(operand):
        return None
    result = 0
    for i in range(len(operand)):
        result = do_algebra_operator(operator[i], operand[i], result)
    return result

if __name__ == "__main__":
    x = [1, 2, 3]
    y = [4, 5, 6]
    xy = [x, y]
    print xy

