def match_parens(lst):
    """
    Aapko do strings ki ek list di gayi hai, dono strings me sirf open
    parentheses '(' ya close parentheses ')' hi hote hain.
    Aapka kaam ye check karna hai ki kya in dono strings ko kisi order me concatenate karne se
    resulting string acchi banegi.
    Ek string S tabhi acchi maani jayegi jab usme saare parentheses balanced ho. Jaise ki: string '(())()' acchi hai, jabki string
    '())' acchi nahi hai.
    Agar acchi string banane ka koi tarika ho to 'Yes' return karo, aur anyatha 'No' return karo.
    Udaharan:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    """
    if len(lst) == 0:
        return "No"
    # get left and right parneters
    first_item = lst[0]
    second_item = lst[1]
    paren_lst = list()
    paren_rst = list()
    if first_item == "(" and second_item == ")":
        print("No")
    else:
        if first_item == ")":
            paren_lst = lst[:-2]
        elif second_item == ")":
            paren_rst = lst[1:]
        else:
            paren_lst = lst[:]
        if check_lst_parens(paren_lst) and check_rst_parens(paren_rst):
            print("Yes")
        else:
            print("No")