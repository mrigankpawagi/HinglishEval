from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Write your code here.
    return [s[:n+1] for n in range(len(string))[::-1] for s in string.partition(string[n:])[1:]]


# Complete the getAllPossibleParentheses function below.
def getAllPossibleParentheses(number_of_inputs: int) -> List[str]:
    if number_of_inputs < 1:
        return []

    return all_prefixes(all_prefixes(str(range(1, number_of_inputs + 1))))
