
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # create the list
    happy_list = list()
    # store the input values in the list
    for c in s:
        happy_list.append(ord(c))
    # using the list, make a function that finds the unique value between the input list
    # if there is only one value, return True
    def is_unique(arr):
        unique = 0
        for value in arr:
            unique = unique ^ value
        return unique
    # check if len of the list is 3 or greather
    if len(happy_list) >= 3:
        # check if the output of the list is not zero
        # if it is, return True for happiness
        if is_unique(happy_list) != 0:
            return(True)

        return False


print(is_happy('a'))
print(is_happy('aa'))
print(is_happy('abcd'))
print(is_happy('aabb'))
print(is_happy('adb'))
print(is_happy('xyy'))
print(is_happy('ab'))
