
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
    def match_parens_2(lst):
        """
        Pares with a string matching parentheses and a keyword.
        """
        for i in range(0, len(lst)):
            match = []
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    match.append(lst[i])
                elif lst[i] == '(':
                    match.append('(')
                elif lst[j] == '(':
                    match