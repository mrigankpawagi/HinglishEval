
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
    if len(s) < 3:
        return False
    set = {}
    l = s
    for i in range(3, len(l) + 1):
        for j in range(0, 3):
            tmp = l[j:j + i]
            if tmp in set:
                return False
            else:
                set.add(tmp)
    return True

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isinstance(n, str):
            n = int(n)
        if n < 0:
            return 0
        if not is_happy(n):
            return 1
        l1 = []
        while n:
            l1.append(n % 10)
            n //= 10
        return self.isHappy(l1[::-1])
