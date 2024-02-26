from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Compute the "AND" of the two inputs
    xor_of_inputs = xors(a, b)
    # Compute the "OR" of the two inputs ANDed with the XOR output
    xor = 0
    for i in range(len(xor_of_inputs)):
        xor = xor_of_inputs[i] | xor
    return xor


if __name__ == '__main__':
    test_outputs = [
        "0000",
        "1100",
        "1111",
        "0101",
        "1010",
        "0100",
        "1001",
        "0001",
    ]

    assert all_test_answers.match(list(map(str, test_outputs))) is None
