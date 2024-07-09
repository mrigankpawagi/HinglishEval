
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
    if not lst: return lst

    # kanan bawah hai me string sa are karo, hai string banane koi usmelik string bacak
    is_last = (len(lst[-1]) > 0)

    def is_match(c1, c2):
        return c1 in '((' and c2 in '()(' and not is_last

    # return [c1 in c2 for c1 in lst]
    lst = sorted(lst, key=len)
    pattern1 = lst
    pattern1 = "".join(["".join(chars) for chars in pattern1])

    # return [is_match(c1, c2) for c1, c2 in zip(pattern1, pattern2)]
    # return True
    # return False

    # return [c in "())" for c in pattern2 if c in "()"]
    return [c.upper() in "()()" for c in pattern1]


print(match_parens(["(", "()()", "()"], ["()()()", "()()", "()("]))
print(match_parens(["()", "()()", "()"]