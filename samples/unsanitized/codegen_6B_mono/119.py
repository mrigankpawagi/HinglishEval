
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
    count = 0
    for i in lst:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count == -1:
            return 'No'
    if count is not 0:
        return 'No'
    else:
        return 'Yes'


assert match_parens(['()(', ')']) == 'Yes'
assert match_parens([')', ')']) == 'No'
assert match_parens(['(', ')']) == 'No'