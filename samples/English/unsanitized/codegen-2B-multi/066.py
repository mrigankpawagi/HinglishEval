
def digitSum(s):
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
    raise NotImplementedError

if __name__ == "__main__":
    assert 8 == digitSum("aBcD")

    with open("data/day17.txt") as f:
        for line in f:
            print "Test case #{0}:".format(line)
            print "  Result:", digitSum(line)
