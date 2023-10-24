
def cycpattern_check(a: str , b: str):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    assert isinstance(a, str) and isinstance(b, str), "invalid inputs" # $_CONTRACT_$
    if a == b:
        return True
    if b == "":
        return True
    for i in range(0, len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False

def check(candidate):

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  candidate("xyzw","xyw") == False
    assert  candidate("yello","ell") == True
    assert  candidate("whattup","ptut") == False
    assert  candidate("efef","fee") == True
    assert  candidate("abab","aabb") == False
    assert  candidate("winemtt","tinem") == True
    assert candidate("abcd","abd") == False
    assert candidate("hello","ell") == True
    assert candidate("whassup","psus") == False
    assert candidate("abab","baa") == True
    assert candidate("efef","eeff") == False
    assert candidate("himenss","simen") == True


check(cycpattern_check)