
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
    for i in xrange(len(s)/3):
        if s[0:i*3] == s[i*3:(i+1)*3]:
            return False
        elif s[( i+1 )*3: i*3+1] == s[( i+1 )*3 +1:( i*3 +1)]:
            return False
        return True
