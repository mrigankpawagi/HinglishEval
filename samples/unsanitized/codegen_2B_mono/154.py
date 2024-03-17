
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
    c=0
    if len(a)==len(b):
        if a==b:
            return True
        l=len(a)-1
        m=l+1
        i=0
        while i<m:
            if a[i]==a[i+1]:
                c+=1
                i+=1
                if (c+m)==l:
                    return True
            else:
                return False
    return False
print(cycpattern_check("helloworld","hello"))