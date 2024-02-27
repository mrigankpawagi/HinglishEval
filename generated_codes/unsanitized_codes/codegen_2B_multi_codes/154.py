
def cycpattern_check(a, b):
    """
    Aapko 2 words diye gaye hain. Aapko True return karna hai agar dusra word ya uske kisi bhi rotation ko pehle word ke substring mein milta hai
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    if len(a)!= len(b):
        return False
    if not a or not b:
        return False
    for x in range(len(a)):
        if a[x]!= b[x]:
            return False
    return True


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        re = ''
        for a in s:
            for b in p:
                if a == b:
                    re += b
                else:
                    if len(re)!= 0:
                        return False

        return len(re) == 0




s = Solution()
s.isMatch('abcd', 'abd')
print s.isMatch('abcd', 'abef')

print s.isMatch('hello', 'ell')










