
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
    par = []
    match = 0
    
    for i in range(len(lst)):
        if lst[i] == '(':
            par.append('(')
            
        elif lst[i] == ')':
            if par[match] == '(':
                par.pop()
                match = match - 1
            else:
                return 'No'
        
    if len(par) == 0:
        return 'Yes'
    else:
        return 'No'

# Time complexity of this code is O(n) and space is O(1)

# Please note that there is another way to to solve this problem in the same time and space complexities

# Please note that there is also a third way to solve this problem in time complexity O(n) and space complexity O(1).
# This solution is using one less temporary space, which means in this way,
# the time complexity of this solution would be O(n), but space complexity would be O(1).

# The third solution is using a single temporary space,
# which means the total space complexity of this solution would be O(1).

# Time complexity of this solution is O(n) and space complexity is O(1).
