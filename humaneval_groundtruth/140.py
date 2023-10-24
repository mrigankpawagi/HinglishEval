
def fix_spaces(text: str):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    assert isinstance(text, str), "invalid inputs" # $_CONTRACT_$
    ans = text
    for i in range(len(text)-1, 2, -1):
        ans = ans.replace(" " * i, "-")
    return ans.replace(" ", "_")

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple"


check(fix_spaces)