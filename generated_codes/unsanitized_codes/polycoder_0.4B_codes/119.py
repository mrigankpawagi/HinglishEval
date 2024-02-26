
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
    lst = [item.replace('(', parenthesis + ')' for item in lst if not item.startswith('('))]
    ls = [item.replace('(', parenthesis) for item in lst if not item.startswith('(')]
    rs = [item.replace('(', parenthesis + ')' for item in lst if not item.endswith(')')])

    if not rs:
        ls = ls[-1:] if not rs else '(...)'
        ls = ls[:-1] if not rs else '['

    return ls[0].replace(rs, r_string)

