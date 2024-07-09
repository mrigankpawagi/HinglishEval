
def words_string(s):
    """
    Aapko ek string di jayegi jisme words commas ya spaces se separated honge. Aapka task hai
    string ko words mein split karna aur words ki array return karna.
    
    Jaise ki:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    
    # 1. aapka saktu aapko karachana ko comma aur space aur space se separated
    # 2. karachana tak split ki array na karachana
    words = s.split()
    
    return words


