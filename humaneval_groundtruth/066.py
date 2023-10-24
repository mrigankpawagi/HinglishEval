
def digitSum(s: str):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    assert type(s) == str, "invalid inputs" # $_CONTRACT_$
    return sum([ord(ch) for ch in s if ch.isupper()])

def check(candidate):

    # Check some simple cases
    assert candidate("") == 0
    assert candidate("abAB") == 131
    assert candidate("abcCd") == 67
    assert candidate("helloE") == 69
    assert candidate("woArBld") == 131
    assert candidate("aAaaaXa") == 153

    # Check some edge cases that are easy to work out by hand.
    assert candidate(" How are yOu?") == 151
    assert candidate("You arE Very Smart") == 327


check(digitSum)