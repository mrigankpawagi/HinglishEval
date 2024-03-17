
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
    # your code here
    return "".join(
        sorted(
            message.lower()
            .replace("a", "4")
            .replace("e", "3")
            .replace("i", "1")
            .replace("o", "0")
            .replace("u", "2")
        )
    )

