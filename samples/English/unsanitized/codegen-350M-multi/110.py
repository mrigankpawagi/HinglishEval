
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    def isEven(num):
        """Compute if "num" is an even number"""
        for value in lst1+lst2:
            if isinstance(value, int) and value % 2 == 1:
                return value == num
        return False

    def isOder(num1, num2):
        """Compute if "num1" > "num2"
        compute whether "num1" is in "num2", which returns "True" if the first is odd,
        and "True" if the second is odd.
        """
        def findOder(num1, num2) :
            "returns odder or odder if "in range(num1, num2) is True"
            return isinstance(num1, int) and isinstance(num2, int) and ((num1 % 2) == 1) and ((num2 % 2) == 1)

        if not (isinstance(num1, int) and isinstance(num2, int)):
            return False

        if findOder(num1, int(num2)):
            if isOder(num1, int(num2)):
                return True
            else:
                return False
        else:
            return False

    if len(lst1) > 2:
        return exchange(lst1, l