
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
    result = operator[0]
    for index, element in enumerate(operator[1:]):
        if (index % 2) == 0:
            result += element
        else:
            result *= element
    return result


if __name__ == '__main__':
    operators = ['+', '*', '-']
    operands = [[2, 32, 5], [4, 48, 34], [7, 6, 10]]
    result = []
    print ("Operator, Operand")
    for operator in range(len(operators)):
        for operand in range(len(operands)):
            print(operator, operand)
            result.append(operator)
        for operator, operator2 in enumerate(result):
            for operand in range(len(operands)):


# Datta list, ki ek element me andar se aar, ki element ke aa le aur aast kiya hai, fir ki humdne
    # list ki daran element se bhi aar
    # array