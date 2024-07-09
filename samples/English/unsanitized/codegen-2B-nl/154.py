
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    firstWords = list(map(lambda x: x.lower(),a))
    secondWords = list(map(lambda x: x.lower(),b))

    for i, secondWord in enumerate(secondWords):
        if firstWords[i] in secondWords:
            return True

# cycpattern_check("abcd","abd") => False
# cycpattern_check("helloh","ell") => False
# cycpattern_check("whassup","psus") => False
# cycpattern_check("abab","baa") => True
# cycpattern_check("efef","eeff") => False
# cycpattern_check("himenss","simen") => True

print(cycpattern_check("abcd","abd"))
print(cycpattern_check("helloh","ell"))
print(cycpattern_check("whassup", "psus"))
print(cycpattern_check("abab", "baa"))
print(cycpattern_check("efef", "eeff"))
print(cycpattern_check("himenss", "simen"))

