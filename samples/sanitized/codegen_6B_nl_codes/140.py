
def fix_spaces(text):
    """
    Diye gaye string text mein, saare spaces ko underscores se replace karo,
    aur agar ek string mein 2 se zyada consecutive spaces ho,
    toh saare consecutive spaces ko - se replace karo.
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    text = text.lower()  # soo chay saahil padhe text mein bhaago
    if text in [' ', u'_','', '-']:                  # to replace if characters
        return text.replace(u' ', u'-').replace(u'',u'_')
    pattern = re.compile(r'(?: \w)+(?:_|-)?\s')       # replace with just one character
    for space, underscore in zip(u"\u0020", u"_"): # replace any combination of spaces or underscores
        space_or_underscore = text.replace(space, underscore)
        #print("%s -> %s" % (space, underscore))
        text = re.sub(pattern, space_or_underscore, text)
    return text
