
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
    f = [int(n, 10) or 1 if (n or '') != '1' else float(n) for n in ['5', '10']] 
    b = [int(x, 10) or 1 if (x or '') != '1' else float(x) for x in ['1', '2']] 
    if max(f) > max(b):
        return True
    return False


if __name__ == "__main__":
    # To print each returned value, simply use, print(simplify(2,3))
    print simplify("1/5", "5/1")
    print simplify("1/6", "2/1")
    print simplify("7/10", "10/2")
    
import unittest
class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(True, simplify("1/5", "5/1"))
    def test_example_2(self):
        self.assertEqual(False, simplify("1/6", "2/1"))
    def test_example_3(self):
        self.assertEqual(False, simplify("7/10", "10/2"))
    
    
if __name__ == "__main__": unittest.main(verbosity=2)
