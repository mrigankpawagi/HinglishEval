
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
    nums = str(set([ord(x) for x in s]))
    tot = 0
    for x in range(len(nums)):
        tot += (tot ^ (tot ^ nums[x]) * int(nums[x]) if nums[x] else nums[x])
    return tot

