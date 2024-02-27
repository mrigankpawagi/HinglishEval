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
    arr = operand
    arr_len = len(arr)
    if arr_len != 0 and operator["+"]:
        for i in range(arr_len - 1):
            y = karke_op(arr[i], arr[i + 1])
            arr[i] = y["value"]
            arr.pop(i + 1)
    elif operator["-"]:
        for i in range(arr_len - 1, -1, -1):
            y = karke_op(arr[i], arr[i + 1])
            arr[i] = y["value"]
            arr.pop(i + 1)
    else:
        for i in range(arr_len):
            if operator["*"]:
                arr[i] = karke_op(operand[i][0], operand[i][1])["value"] * karke_op(
                    arr[i], operand[i + 1]
                )