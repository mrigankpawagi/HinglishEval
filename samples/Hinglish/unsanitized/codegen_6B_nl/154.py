
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
    #print('a :', a,'\n b : ', b);
    for i in range(len(a[1:])):
        print('substring : ', a[:i+1],'\nsubstring : ',a[i:])


for i in range(1,10) :
    word = chr(i)
    pattern = list(string.ascii_lowercase)
    word.lower()
    #print(word)
    s = pattern + list(word)
    for i in range(0,len(s)-1):
        for j in range(len(s)):
            #print(*s[i:j],'\n',*s[j:i+1],'\n')
            for substring in [s[i:j+1],s[j:i+1]]:
                if cycpattern_check(substring,word):
                    print(word,substring,substring in s,"y" if (j<i) else "n")
            print