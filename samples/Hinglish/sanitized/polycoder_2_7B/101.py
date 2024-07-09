
def words_string(s):
    """
    Aapko ek string di jayegi jisme words commas ya spaces se separated honge. Aapka task hai
    string ko words mein split karna aur words ki array return karna.
    
    Jaise ki:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    s = s.replace(" ", "").split()
    res = []
    for w in s:
        if w[0] =='':
            w_list = w[1:].split(',')
            w_value = tuple(w[i+1:i+1+len(w_list) for i in range(1, len(w_list)+1)])
            w_value2 = "(" + ",".join("".join(w_value) for w_value in w_list) + ")"
            res.append(w_value2)
        else:
            res.append(w)
    return res
