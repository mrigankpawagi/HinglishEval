
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    from mako.template import Template
    from mako import exceptions
    import re
    ch = _convert_ch(s[0])
    subtokens = re.split('([a-z]+)',ch) # Convert a letter to a letter or string
    num_subs2 = [ch.count('b')]+range(2,ch.count(ch)+1) # Add a 2+1 bit mask
    for s in subtokens:
        s = s.strip()
        substr,_,_ = "".join(s[:_]).split(':',maxsplit=1)
        substr = re.escape(substr)
        #print substr,_,substr
        char_match = re.compile("-?[A-Z]+")
        if char_match.match(substr):
            #print "1"
            substr = substr.replace(char_match.pattern,'-')
            num_subs2.append(char_match.match(str(substr)).group(0))
            #print "2"
        elif substr[:_] in num_subs2:
            #print "3"
            num_subs2.remove(substr[:_])
            #print "4"
            substr = char_match.findall(char_match.pattern.replace("-", "_"))[0]
            char_match = re.compile("-?[A-Z]+") # Remove the 'b'
            for c in substr:
                try:
                    tokens = []
                    ch = unicode(a16)
                    tokens.append(("b