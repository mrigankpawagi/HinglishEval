
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
    string_length = len(s)
    if (string_length < 2): return False
    if (string_length >= 3 and all(x not in chr(ord(x)) for x in s)) or (string_length >= 5 and any(x not in chr(ord(x)) for x in s)):
        return True
    else:
        return False


