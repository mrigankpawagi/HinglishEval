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
    result = []
    for c in message:
        if unicodedata.category(c)[1] == "Lu":
            ord(c)
        elif (unicodedata.category(c)[1] == "Ll") or (
            unicodedata.category(c)[1] == "Lt"
        ):
            unicodedata.utf8(c)
        else:
            ord(c)
    return "".join([str(n) for n in list(result)])