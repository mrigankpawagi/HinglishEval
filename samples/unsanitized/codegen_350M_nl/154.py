
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
    return True if a > b else False


class Cycpattern(object):
    """
    The base class of a cycpattern
    """
    def __init__(self, **kwargs):
        self.test = True
        with testpy.CycPattern() as e:
            for (key, value) in e.mutable_tests() :
                if key == "test" :
                    self.test = False
                else :
                    e.mutable_tests[key]()


class Cycword(object):
    """
    Aapko 2 words diye gaye hain. Aapko True return karna hai agar dusra word ya uske kisi bhi rotation ko pehle word ke substring mein milta hai cycword
    """
    def __init__(self, test):

    def test(t, key, text):

        for word in t.mutable_words