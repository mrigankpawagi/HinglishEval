def encode(message):
    """
    Ek function likho jo ek message leta hai, aur usko aise encode karta hai
    ki wo saare letters ki case ko swap kar deta hai, saare vowels ko
    unke aage wale 2nd letter se replace kar deta hai english alphabet mein.
    Sirf letters maan lo.
    Udaharan:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Code here
    m = list(message)
    for i in range(len(m)):
        if m[i] in vowels:
            m = list(m)
            m[i] = "x"
            if len(m[i]) == 1:
                m[i] = "x"
            m[i] = "y" + m[i][1:]
        elif m[i] in consonants:
            m = list(m)
            if m[i] == "s":
                m[i] = "t"
            if m[i] == "x":
                m[i] = "z"
            if m[i] == "y":
                m[i] = "z"
        # else:
        #     m = '?'
    # print(''.join(m))
    return "".join(m)