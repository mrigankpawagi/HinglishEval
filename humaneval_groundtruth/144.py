
def simplify(x: str, n: str):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    def contract(x): # $_CONTRACT_$
        assert isinstance(x, str), "invalid inputs" # $_CONTRACT_$
        xs = x.split("/") # $_CONTRACT_$
        assert len(xs) == 2, "invalid inputs" # $_CONTRACT_$
        assert xs[0].isdigit() and int(xs[0]) > 0, "invalid inputs" # $_CONTRACT_$
        assert xs[1].isdigit() and int(xs[1]) > 0, "invalid inputs" # $_CONTRACT_$
    contract(x) # $_CONTRACT_$
    contract(n) # $_CONTRACT_$

    x1, x2 = map(int, x.split("/"))
    n1, n2 = map(int, n.split("/"))
    return (x1 * n1) % (x2 * n2) == 0

def check(candidate):

    # Check some simple cases
    assert candidate("1/5", "5/1") == True
    assert candidate("1/6", "2/1") == False
    assert candidate("5/1", "3/1") == True
    assert candidate("7/10", "10/2") == False
    assert candidate("2/10", "50/10") == True
    assert candidate("7/2", "4/2") == True
    assert candidate("11/6", "6/1") == True
    assert candidate("2/3", "5/2") == False
    assert candidate("5/2", "3/5") == False
    assert candidate("2/4", "8/4") == True


    # Check some edge cases that are easy to work out by hand.
    assert candidate("2/4", "4/2") == True
    assert candidate("1/5", "5/1") == True
    assert candidate("1/5", "1/5") == False


check(simplify)