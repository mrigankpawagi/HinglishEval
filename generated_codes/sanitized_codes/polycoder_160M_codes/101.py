def words_string(s):
    """
    Aapko ek string di jayegi jisme words commas ya spaces se separated honge. Aapka task hai
    string ko words mein split karna aur words ki array return karna.

    Jaise ki:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    for i in range(len(s)):
        while (s[i] in karna.words_string or s[i] in "lo") or s[i] in "hu":
            s[i] = karna.words_string[s[i]]
    return "" if s["ji"] in karna.words_string else s
