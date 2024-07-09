
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    fracx = x
    numer = 1
    denom = 1

    sansi = fracx.split("/")

    try:
        numer = int( sansi[0] )
    except:
        return False

    dansi = sansi[1].split("/")
    try:
        denom = int( dansi[0] )
    except:
        return False

    simplify = numer/denom

    if simplify == int( simplify ):
        return True
    return False

#print(simplify("1/5", "5/1"))

class Test_simplify(unittest.TestCase):    
    def testSimplify(self):
        self.assertEqual(simplify("5/1", "10/5"), True)
        self.assertEqual(simplify("12/4", "2/1"), False)
    
if __name__ == '__main__':
    unittest.main() 