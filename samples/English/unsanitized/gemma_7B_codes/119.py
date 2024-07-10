
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
        return 'Yes'
    if len(lst) % 2 != 0:
        return 'No'
    stack = []
    def paranthesis_balanced(exp):
        for ch in exp:
            if ch == '(':
                stack.append('(')
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
    def matching(lst):
        out_of_scope = False
        for exp in lst:
            if out_of_scope:
                if not paranthesis_balanced(exp):
                    return 'No'
            else:
                if paranthesis_balanced(''.join(exp)):
                    out_of_scope = True
        return 'Yes'
    return matching(lst)
