
def words_string(s):
    """
    Aapko ek string di jayegi jisme words commas ya spaces se separated honge. Aapka task hai
    string ko words mein split karna aur words ki array return karna.
    
    Jaise ki:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    arr = []
    string_words = ['','', 'Hi','my', 'name', 'is', 'John']
    while s!= '':
        arr.append(s.lower())
        s = s[1:]
        
    for s, w in zip(arr, string_words):
        try:
            arr.insert(0, s +'')
            s = w
            ws_len = len(w)
        except IndexError:
            k = ws_len
            ws = str(w)
        else:
            k = len(w)
            ws = ws[0:ws_len]
            t = w +''
        arr.append(t)
        
    for w in arr:
        if w =='':
            continue
        t = []