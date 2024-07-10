
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
    result = ""
    for i in range(len(operator)):
            result += str(operand[i]) + str(operator[i])
    result += str(operand[len(operand) - 1])
    try:
        exec(result)
        return result
    except Exception:
        return 0


# My approach:
    """
import ast, operator
def do_algebra(operator, operand):
   list = len(operator)
   result = 0
   if list == 1:
       result = eval(operator.pop() + str(operand.pop()))
   elif list == 2:
       result = eval(str(operand.pop())+' '+ operator.pop()+' '+str(operand.pop()))
   else:
       for i in range(len(operator)):
           string = str(operand.pop())+' '+ operator.pop() +' '+str(operand.pop())
       result =  eval(string)
   return result
    """
