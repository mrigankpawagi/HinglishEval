
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
    s = s.upper()
    letter_list = [l for l in s]

    if len(s) <= 3:
        return False

    for i in range(len(s)-2):
        j = 0
        for i in range(1, letter_list.index(i)):
            if letter_list[i]!= letter_list[j]:
                return False

    return True


