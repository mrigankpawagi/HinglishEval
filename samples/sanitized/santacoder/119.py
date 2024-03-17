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
    # Nai karne sarjuna ki li
    if len(lst) == 0:
        return "Yes"
    else:
        if lst[0] == "(":
            # Nai parenthesiye parere na karne sarjuna.
            if (len(lst) == 1) or (len(lst[1:]) == 0):
                return "Yes"
            else:
                second = lst[1:]
                # nai parenthesiya karo yon, ek list nare
                # Naye ek starek hai string
                return match_parens(second)
