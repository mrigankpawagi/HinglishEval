
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
    # If the denominator of the formula is > 0, there are four ways to calculate the
    # factor of the expression for which it must be simplified:

    # 2. For every existing term x in the expression, find all denominators that
    # have this numerator and denominator, and compute the factor that can be
    # simplified by multiplying all of those numerators together.
    terms = [term for (term, expr) in enumerate(x) if expr >= 0]
    result = [n for (term, expr) in enumerate(x) if expr >= 0]
    factor = 1
    for i in range(len(result)):
        new_terms = [term
            for (term, expr) in enumerate(x) if expr >= 0]
        new_result = [n
            for (term, expr) in enumerate(x) if expr >= 0]
        new_factor = 0
        for i in range(len(new_terms)):
            new_terms[i] = simplify(new_terms[i], new_result[i])
        factor *= len(new_terms)
        new_result = [n
            for (term, expr) in enumerate(x) if expr > 0]
        new_factor = len(new_result[i])
        for i in range(len(new_terms)):
            new_terms[i] = [x * factor ** i]
        result[i] = list(new_terms[i])