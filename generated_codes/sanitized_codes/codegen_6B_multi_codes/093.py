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
    message = message.upper()
    code = []
    # Code has to be sorted, so there is no use if the list is not
    # alphabetically sorted from start to end
    letterDict = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25,
    }
    for character in message:
        letterPosition = 0
        for letter in list(alphabet):
            if character == letter:
                code.append(letterDict[letter])
                letterPosition += 1
                for i in range(letterPosition):
                    # Code won't allow the letters being
                    # same, need to skip for code
                    letterPosition += 1
                break
        letterPosition += 1
    return "".join(code)