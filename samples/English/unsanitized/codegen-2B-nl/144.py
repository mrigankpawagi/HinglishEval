
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
    numerator_x, denominator_x = [_ for _, _ in str(x)]

    if numerator_x == 0:
        raise ValueError("x*n" + str(x))    # x*n!= 0
    elif denominator_x == 0:
        raise ValueError("x/n" + str(x))    # x/n!= 1/1
    elif (numerator_x == denominator_x):
        return True
    else:
        return False

I have tried your code and it works with a list:
invalid_list = ["3/5", "5/4", "2/9"]
simplify("1/*1/13", "1/*7")

and:
invalid_list = ["1/3", "3/4", "2/3"]
simplify("1/*2/3", "1/*1/3")  # returns True
simplify("1/*3", "1/*1/3")    # returns False

but returns False:
invalid_list = []
invalid_list = ["1/2", "2/1", "1/2"]
simplify("1/2/*1", "1/*1")  # returns False

