
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
    # add all element in list
    def add_digits(number):
        digit_list = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        for digit in number[:-1]:
            currentNumber =  digit_list.pop(digit_list.index(digit) + (digit + (digit == '0')))
            digit_list.pop()
        additive = list(str(int(number)+int(operator))[2:])
        additive = [2] + additive
        return ['+', '] + additive + ['-']
    
    # Subtract element from list
    def sub_digits(number):
        digit_list = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

        if operator == "*":
            number_to_add = operator_list[:-1]
            for item in number_to_add:
                for digit in str(item