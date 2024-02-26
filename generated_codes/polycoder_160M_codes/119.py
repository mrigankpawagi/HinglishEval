
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
    match_parens(['(', ')']) == 'Yes'
    match_parens(['(", ")", ')']) == 'No'

    # Aapko, Gashk, Hani, Hang, Han, Gay, Hanga, Hant, Haka, Hanana, Saaharan
    if "k" in lst:  # Kappa
        del lst.pop(0)
        lst += " (")
        for s in re.split("(?m)+", lst, re.IGNORECASE):  # I'm gonna just be a string
            s2 = s.replace("[.", "_")
            # Aapko, Gashk, Hani, Hang, Gay, Han, Gay, Hanga, Hant, Haka, Hanana, Saaharan
            match_parens(s2.split(""))
   